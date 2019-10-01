import requests
from lxml import html

XPATH = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')


class GithubLogin(object):
    def __init__(self):
        self.headers={
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 73.0.3683.103 Safari / 537.36',
            'Referer':'https://github.com/',
            'Host':'github.com'
        }
        self.login_url='https://github.com/login'
        self.post_url='https://github.com/session'
        self.logined_url='https://github.com/settings/profile'
        self.session=requests.Session()

    def token(self):
        response=self.session.get(self.login_url,headers=self.headers)
        selector=html.etree.HTML(response.text)
        print(response.text)
        token=selector.xpath('//input[@name="authenticity_token"]/@value')
        print(token)
        return token

    def login(self,email,password):
        post_data={
            'commit':'Sign in',
            'utf8':'✓',
            'authenticity_token':self.token(),
            'login':email,
            'password':password
        }
        response=self.session.post(self.post_url,data=post_data,headers=self.headers)
        if response.status_code==200:
            self.dynamics(response.text)

        response = self.session.get(self.login_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self,html):
        selector=html.etree.HTML(html)
        dynamics=selector.xpath('//div[contains(@class,"news)]//div[contains(@class,"alert)]')
        for item in dynamics:
            dynamic=' '.join(item.xpath('.//div[@class="title"]//text()'))
            print(dynamic)

    def profile(self,html):
        selector = html.etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email= XPATH
        print(name,email)


if __name__ == '__main__':
    github_login=GithubLogin()
    github_login.login(email='1413476657@qq.com',password='Redback1020')

