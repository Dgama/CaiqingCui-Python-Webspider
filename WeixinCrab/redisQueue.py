from pickle import dumps,loads
from WeixinCrab.WeixinRequest import WeixinRequest
from redis import StrictRedis
from WeixinCrab.weixin_settings import *

class RedisQueue():
    def __init__(self):
        """
        初始化Redis
        """
        self.db=StrictRedis(host=REDIS_HOST,port=REDIS_PORT)

    def add(self,request):
        """
        向队列中添加序列化的请求
        :param request:
        :return:
        """

        if isinstance(request,WeixinRequest):
            return loads(self.db.rpush(REDIS_KEY,dumps(request)))
        return False

    def pop(self):
        """
        取出下一个request并反序列化
        :return:
        """
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop(REDIS_KEY))
        else:
            return False

    def empty(self):
        return self.db.llen(REDIS_KEY)==0