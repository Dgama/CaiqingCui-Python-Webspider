from requests import Session
from WeixinCrab.redisQueue import RedisQueue
from WeixinCrab.WeixinRequest import WeixinRequest
from urllib.parse import urlencode
from WeixinCrab.weixin_settings import *
from requests import ReadTimeout,ConnectionError
from pyquery import PyQuery as pq

class Spider():
    base_url='http://weixin.sogou.com/weixin'
    keyboard='NBA'
    headers={
    'Host': 'weixin.sogou.com',
    'Connection': 'keep - alive',
    'Cache - Control': 'max - age = 0',
    'Upgrade - Insecure - Requests': '1',
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 73.0.3683.103 Safari / 537.36',
    'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept - Language': 'zh - CN, zh;q = 0.9, ja;q = 0.8, en;q = 0.7',
    'Cookie': 'SUV = 00227016CA7813765BE62EE86D092231;SUID = 441378'
              'CA2313940A000000005C036F8D;ssuid = 6514828104;CXID = 7BBA7AEB60BFAE4C82CA555B36DE04C9;'
              'IPLOC = CN3100;ld = SZllllllll2trN6FlllllVhHLSGlllllhXkFNZllll9llllljklll5 @ @ @ @ @ @ @ @ @ @;'
              'ABTEST = 2 | 1557024893 | v1;weixinIndexVisited = 1;sct = 1;SNUID = 2A2B5A2F14109C0F097A3C7315A4C463;'
              'ppinf = 5 | 1557030949 | 1558240549 | dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyOmJifGNydDoxMDoxNTU3MDMwOTQ5fHJlZm5pY2s6MjpiYnx1c2VyaWQ6NDQ6bzl0Mmx1QmVkVUxPeEl6by1Pb2xnVGVyWlpmc0B3ZWl4aW4uc29odS5jb218;'
              'pprdig = HE8rxaqjUGC2hBM0GKg1ivN63iF4zqMdbPG1pTR9FCEukh8msKiq7ZSwnvYCaCTVWi8nVjuzPJ6XSg3uUfWg4E6KaRtkV1RxUKmG8d_SOOazjFlMIGxO - Dzqg5ecqoSuyt1d_knTZB0s0RgERJRwDg3UcTl0eUVbBrbEMgOjgw4;'
              'sgid = 27 - 40495445 - AVzOaCW7SO6Vhcib2AD7s2xs;ppmdig = 1557035538000000b90c7468887b0c3f9e6033adc884cacd',
    }

    session=Session()
    queue=RedisQueue()

    def start(self):
        """
        初始化工作
        :return:
        """
        self.session.headers.update(self.headers)
        start_url=self.base_url+'?'+urlencode({'query':self.keyboard,'type':2})
        weixin_request=WeixinRequest(url=start_url,callback=self.parse_index,need_proxy=True)
        #调度第一个请求
        self.queue.add(weixin_request)

    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty():
            weixin_request=self.queue.pop()
            callback=weixin_request.callback
            print('Schedule',weixin_request.url)
            response=self.request(weixin_request)
            if response and response.status_code in VALID_STATUSES:
                results=list(callback(response))
                if results:
                    for result in results:
                        print('New result',result)
                        if isinstance(result,WeixinRequest):
                            self.queue.add(result)
                        if isinstance(result,dict):
                            self.mysql.insert('article',result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

    def requests(self,weixin_request):
        """
        执行请求
        :param weixin_request: 请求
        :return:
        """
        try:
            if weixin_request.need_proxy:
                proxy=get_proxy()
                if proxy:
                    proxies={
                        'http':'http://'+proxy,
                        'https':'https://'+proxy
                    }
                    return self.session.send(weixin_request.prepare(),timeout=weixin_request.timeout,allow_redirects=False,proxies=proxies)
            return self.session.send(weixin_request.prepare(),timeout=weixin_request.timeout,allow_redirects=False)
        except (ConnectionError,ReadTimeout) as e:
            print(e.args)
            return False

    def parse_index(self,response):
        """
        解析索引页
        :param response:响应
        :return:
        """
        doc=pq(response.text)
        items=doc('.news-box .new-list li .txt-box h3 a'.items())
        for item in items:
            url=item.attr('href')
            weixin_request=WeixinRequest(url=url,callback=self.parse_detail)
            yield weixin_request
        next=doc('#sogou_next').attr('href')
        if next:
            url=self.base_url+str(next)
            weixin_request=WeixinRequest(url=url,callback=self.parse_index,need_proxy=True)
            yield weixin_request

    def parse_detail(self,response):
        """
        解析详情页
        :param response:
        :return:
        """
        doc=pq(response.text)
        data={
            'title':doc('.rich_media_title').text(),
            'content':doc('.rich_media_content').text(),
            'date':doc('#post-date').text(),
            'nickname':doc('#js_profile_qrcode>div>strong').text(),
            'wechat':doc('#js_profile_qrcode>div>p:nth-child(3)>span').text()
        }
        yield data

    def error(self,weixin_request):
        """
        处理错误
        :param weixin_request:
        :return:
        """
        weixin_request.fail_time=weixin_request.fail_time+1
        print('Request Failed',weixin_request.fail_time,'Times',weixin_request.url)
        if weixin_request.fail_time<MAX_FAILED_TIME:
            self.queue.add(weixin_request)

    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()

if __name__ == '__main__':
    spider=Spider()
    spider.run()