from WeixinCrab.weixin_settings import *
import pymysql

class WeixinMysql():
    def __init__(self,host=MYSQL_HOST,port=MYSQL_PORT,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DATABASE):
        """
        初始化数据库
        :param host:
        :param port:
        :param username:
        :param password:
        :param database:
        """
        try:
            seld.db=pymysql.connect(host,username,password,database,charset='utf8',port=port)
            self.cursor=self.db.cursor()
        except pymysql.MySQLError  as e:
            print(e.args)

    def insert(self,table,data):
        """
        插入数据
        :param table:
        :param data:
        :return:
        """
        keys=','.join(data.keys())
        values=','.join(['%s']*len(data))
        sql_query='insert into %s(%s) values (%s)'%(table,keys,values)
        try:
            self.cursor.execute(sql_query,tuple(data.values()))
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()
