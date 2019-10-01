from multiprocessing import Process
from redis_api import app
from Getter import Getter
from Tester import Tester
import time
from setttings import *

class Scheduler():
    def schedule_tester(self,cycle=TESTER_CYCLE):
        """
        定时测试代理
        :param cycle:
        :return:
        """
        tester=Tester()
        while True:
            print('测试机器运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self,cycle=GETTER_CYCLE):
        """
        定时获取代理
        :param cycle:
        :return:
        """
        getter=Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep()

    def schedule_api(self):
        """
        开启api
        :return:
        """
        app.run(API_HOST,API_PORT)

    def run(self):
        print('代理池开始运行')

        if API_ENABLED:
            api_process=Process(target=self.schedule_api())
            api_process.start()

        if TESTER_ENABLED:
            test_process=Process(target=self.schedule_tester())
            test_process.start()

        if GETTER_ENABLED:
            getter_process=Process(target=self.schedule_getter())
            getter_process.start()

