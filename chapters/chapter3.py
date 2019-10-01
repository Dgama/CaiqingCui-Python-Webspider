import urllib.request
import urllib.parse
import socket
import urllib.error
import http.cookiejar
from urllib.robotparser import RobotFileParser
import requests
import re

# response = urllib.request.urlopen('http://python.org')
#
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')

# try:
#     response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')
# print(response.read())

# request=urllib.request.Request('http://python.org')
# response=urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# url='http://httpbin.org/post'
# dict={'name':'Germy'}
# data=bytes(urllib.parse.urlencode(dict),encoding='utf8')
# req=urllib.request.Request(url=url,data=data,method='POST')
# req.add_header('User-Agent','Mozilla/4.0(compatible;MISE 5.5;Windows NT)')
# response=urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# cookie=http.cookiejar.CookieJar()
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+'='+item.value)

# filename='cookies.txt'
# cookie=http.cookiejar.MozillaCookieJar(filename)
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

# filename='cookies.txt'
# cookie=http.cookiejar.MozillaCookieJar()
# cookie.load(filename,ignore_expires=True,ignore_discard=True)
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# result=urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result),result,sep='\n')

# data=['scheme','netloc','path','params','query','fragment']
# url=urllib.parse.urlunparse(data)
# print(type(url),url)

# params={'name':'ger','age':22}
#
# base_url='http://www.baidu.com?'
# url=base_url+urllib.parse.urlencode(params)
# print(url)
# query='name=ger&age=22'
# print(urllib.parse.parse_qs(query))
# print(urllib.parse.parse_qsl(query))

# url='http://www.baidu.com/s?wd='+urllib.parse.quote('壁纸')
# print(url)
# print(urllib.parse.unquote(url))

# rp=RobotFileParser()
# rp.set_url("http://www.jianshu.com/robot.txt")
# rp.read()
# print(rp.can_fetch('*','http://www.janshu.com/p/b67554025d7d'))

# r=requests.get("https://www.baidu.com/")
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(type(r.cookies))
# print(r.cookies)

# data={'name':'ger','age':'22'}
# r=requests.get("http://httpbin.org/get",params=data)
# print(r.text)

# r=requests.get('http://httpbin.org/get')
# print(r.text)
# print(type(r.json()))
# print(r.json())

# headers={'User-Agent':',Mozilla/5.0(Macintosh;Intel Mac OS X 10_11_4)AppleWebKit/537.36(KHTML,Like Gecko)Chrome/52.0.2743.116 Safari/537.36'
#          }
# r=requests.get("https://www.zhihu.com/explore",headers=headers)
# pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles=re.findall(pattern,r.text)
# print(titles)

# r=requests.get("https://github.com/favicon.ico")
# with open('favicon.ico','wb') as f:
#     f.write(r.content)

# data={'name':'good'}
# r=requests.post('http://httpbin.org/post',data=data)
# print(r.text)

# r=requests.get('http://www.jianshu.com')
# exit() if  not r.status_code==requests.codes.ok else print('Request Successfully')

# files={'files':open('favicon.ico','rb')}
# r=requests.post('http://httpbin.org/post',files=files)
# print(r.text)

# r=requests.get('https://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+value)

# headers={
#     'Cookie':'_xsrf=gbmdDr7GlSJIvifgzNVknyjPwWMfCh4W; _zap=70ec5a60-234a-4996-9313-2fc998e79839; d_c0="APBnHpVfew6PTu6'
#               'utbgZ3dev_zmEZNlOIPo=|1541577615"; z_c0="2|1:0|'
#               '10:1544010355|4:z_c0|92:Mi4xREVjcEF3QUFBQUFBOEdjZWxWO'
#               'TdEaVlBQUFCZ0FsVk5jd2oxWEFCR1RyTFBMajFWR21oMjZtbjJVTk1mZDBzTFB3|'
#               'e7ddcff50bf2978ade073d4a5589a498c8b23e0700cd4c2af77de5a5c'
#               'a7075e5"; tst=r; q_c1=b37ce6388bd842daa270319e224f2da5|15560'
#               '27360000|1549329029000; __utma=51854390.287900563.1556027362.1556027362.1556027362.1'
#               '; __utmb=51854390.0.10.1556027362; __utmz=51854390.1556027362.1.1.utmcsr=(direct)|utm'
#               'ccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20160620=1^3=entry'
#               '_date=20160620=1; tgw_l7_route=4860b599c6644634a0abcd4d10d37251',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like'
#                  ' Gecko) Chrome/73.0.3683.103 Safari/537.36',
#     'Host':'www.zhihu.com'
# }
# r=requests.get('https://www.zhihu.com',headers=headers)
# print(r.text,r.status_code,sep='\n')

# cookies='_xsrf=gbmdDr7GlSJIvifgzNVknyjPwWMfCh4W; _zap=70e' \
#         'c5a60-234a-4996-9313-2fc998e79839; d_c0="APBnHpVfew6PTu6utbg' \
#         'Z3dev_zmEZNlOIPo=|1541577615"; z_c0="2|1:0|10:1544010355|4:z_c0|92:Mi4xREVjcE' \
#         'F3QUFBQUFBOEdjZWxWOTdEaVlBQUFCZ0FsVk5jd2oxWEFCR1RyTFBMajFWR21oMjZtbjJVTk1mZDBz' \
#         'TFB3|e7ddcff50bf2978ade073d4a5589a498c8b23e0700cd4c2af77de5a5ca7075e5"; tst=r; q_c1=' \
#         'b37ce6388bd842daa270319e224f2da5|1556027360000|1549329029000; __utma=51854390.2' \
#         '87900563.1556027362.1556027362.1556027362.1; __utmb=51854390.0.10.1556027' \
#         '362; __utmz=51854390.1556027362.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _' \
#         '_utmv=51854390.100--|2=registration_date=20160620=1^3=entry_date=20160620=1; tgw_l7_r' \
#         'oute=4860b599c6644634a0abcd4d10d37251'
#
# jar=requests.cookies.RequestsCookieJar()
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like'
#                  ' Gecko) Chrome/73.0.3683.103 Safari/537.36',
#     'Host':'www.zhihu.com'
# }
# for cookie in cookies.split(';'):
#     key,value=cookie.split('=',1)
#     jar.set(key,value)
# r=requests.get('https://www.zhihu.com',cookies=jar,headers=headers)
# print(r.text)

# s=requests.session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)

# response=requests.get('https://www.12306.cn')
# print(response.status_code)

# url='http://www.httpbin.org/post'
# data={'name':'hhh','age':22}
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like'
#                  ' Gecko) Chrome/73.0.3683.103 Safari/537.36',
#     'Host':'www.zhihu.com'}
# s=requests.sessions.Session()
# req=requests.Request('POST',url,data=data ,headers=headers)
# prepped=s.prepare_request(req)
# r=s.send(prepped)
# print(r.text)

# content='Hello 123 4567 World_this is a Regex Demo'
# print(len(content))
# result=re.match('^Hello\s(\d+)\s(\d{4})\s\w{10}',content)
# print(result)
# print(result.group())
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))
# print(result.span())

# content='''Hello 123 4567 World_t
#         his is a Regex Demo'''
# print(len(content))
# result=re.match('^He(.*?)(\d+)(.*?)$',content,re.S)
# print(result)
# print(result.group())
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))
# print(result.span())

# print(len(content))
# result=re.match('^He(.*?)(\d+)(.*?)$',content,re.S)
# print(result)
# print(result.group())
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))
# print(result.span())

