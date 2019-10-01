import redis
import random

REDIS_HOST='remoteaddress'
REDIS_PASSWORD='foobared'
REDIS_PORT=6379
PROXY_KEY='adsl'

class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD,proxy_key=PROXY_KEY):
        """
        初始化Redis连接
        :param host:
        :param port:
        :param password:
        :param proxy_key:
        """
        self.db=redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)
        self.proxy_key=proxy_key

    def set(self,name,proxy):
        """
        设置代理
        :param name:
        :param proxy:
        :return:
        """
        return self.db.hset(self.proxy_key,name,proxy)

    def get(self,name):
        """
        获取代理
        :param name:
        :return:
        """
        return self.db.hget(self.proxy_key,name)

    def count(self):
        """
        获取代理总数
        :return:
        """
        return self.db.hlen(self.proxy_key)

    def remove(self,name):
        """
        删除代理
        :param name:
        :return:
        """
        return self.db.hdel(self.proxy_key,name)

    def name(self):
        """
        获取主机名称列表
        :return:
        """
        return self.db.hkeys(self.proxy_key)

    def proxies(self):
        """
        获取代理列表
        :return:
        """
        return self.db.hvals(self.proxy_key)

    def random(self):
        """
        随机获取代理
        :return:
        """
        proxies=self.proxies()
        return random.choice(proxies)

    def all(self):
        """
        获取字典
        :return:
        """
        return self.db.hgetall(self.proxy_key)