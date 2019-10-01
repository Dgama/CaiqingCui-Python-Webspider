import redis
from  random import choice
from setttings import *

class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        """
        初始化
        :param host:
        :param port:
        :param password:
        """
        self.db=redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def add(self,proxy,score=INITIAL_SCORE):
        """
        添加代理
        :param proxy:
        :param score:
        :return:
        """
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)

    def random(self):
        """
        随机获取有效代理，首先尝试分最高的代理，如果高分不存在，则按照排名获取，否则异常
        :return:
        """
        result=self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MIN_SOCRE)
        if len(result):
            return choice(result)
        else:
            result=self.db.zrevrange(REDIS_KEY,0,100)
            if len(result):
                return choice
            else:
                raise PoolEmptyError

    def decrease(self,proxy):
        """
        代理值减一分，分数小于最小值，则代理删除
        :param proxy:
        :return:
        """
        score=self.db.zscore(REDIS_KEY,proxy)
        if score and score>MIN_SOCRE:
            print('代理',proxy,'当前分数',score,'减1')
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY,proxy)

    def exists(self,proxy):
        """
        判断是否存在
        :param proxy:
        :return:
        """
        return not self.db.zscore(REDIS_KEY,proxy)==None

    def max(self,proxy):
        """
        将代理设置成满分
        :param proxy:
        :return:
        """
        print('代理', proxy, '可用，设置成', MAX_SCORE)
        return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def count(self):
        """
        获取数量
        :return:
        """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        获取全部代理
        :return:
        """
        return self.db.zrangebyscore(REDIS_KEY,MIN_SOCRE,MAX_SCORE)