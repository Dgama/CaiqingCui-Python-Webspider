import re
import time
import requests
from requests.exceptions import ConnectionError, ReadTimeout
from redis_func import RedisClient
import subprocess

#拨号网卡
ADSL_IFNAME='ppp0'

TEST_URL='http://www.baidu.com'
TEST_TIMEOUT=20
ADSL_CYCLE=100
ADSL_ERROR_CYCLE=5

#ADSL 命令
ADSL_BASH='adsl-stop;adsl-start'

PROXY_PORT=8888

#客户端唯一标识
CLIENT_NAME='adsl1'

class Sender():
    def get_ip(self,ifname=ADSL_IFNAME):
        """
        获取本机ip
        :param ifname:
        :return:
        """
        (status,output)=subprocess.getstatusoutput('ifconfig')
        if status==0:
            pattern=re.compile(ifname+'.*?inet.*?(\d+\.\d+\.\d+\.\d+).*?netmask',re.S)
            result=re.search(pattern,output)
            if result:
                ip=result.group(1)
                return  ip

    def test_proxy(self,proxy):
        """
        测试代理
        :param proxy:
        :return:
        """
        try:
            response=requests.get(TEST_URL,proxy={
                'http':'http://'+proxy,
                'https':'https://'+proxy
            },timeout=TEST_TIMEOUT)
            if response.status_code==200:
                return True
        except (ConnectionError,ReadTimeout):
            return False

    def remove_proxy(self):
        """
        移除代理
         :param self:
        :return:
        """
        self.redis=RedisClient()
        self.redis.remove(CLIENT_NAME)
        print('successfully removed proxy')

    def set_proxy(self,proxy):
        """
        设置代理
        :param self:
        :return:
            """
        self.redis=RedisClient()
        if self.redis.set(CLIENT_NAME,proxy):
            print('successfully set proxy',proxy)

    def adsl(self):
        """
        拨号主进程
        :return:
        """

        while True:
            print('ADSL start,Remove Proxy, Please wait')
            self.remove_proxy()
            (status,output)=subprocess.getstatusoutput(ADSL_BASH)
            if status==0:
                print('ADSL Successfully')
                ip=self.get_ip()
                if ip:
                    print('Now ip',ip)
                    print('Testing Proxy,Please Wait')
                    proxy='{ip}:{port}'.format(ip=ip,port=PROXY_PORT)
                    if self.test_proxy(proxy):
                        print('valid proxy')
                        self.set_proxy(proxy)
                        print('sleeping')
                        time.sleep(ADSL_CYCLE)
                    else:
                        print('invalid proxy')

                else:
                    print('Get IP failed, Re Dialing')
            else:
                print('ADSL Failed,Please Check')
                time.sleep(ADSL_ERROR_CYCLE)

def run():
    sender=Sender()
    sender.adsl()