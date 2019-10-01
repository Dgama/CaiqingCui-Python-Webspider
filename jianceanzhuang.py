# from bs4 import BeautifulSoup
# soup=BeautifulSoup('<p>Hello<p>','lxml')
# print(soup.p.string)
#
# mongod --bind_ip 0.0.0.0 --logpath "E:\Mongodb\Server\4.0\logs\mongodb.log" --logappend --dbpath "E:\Mongodb\Server\4.0\data\db"--port 27017 --serviceName "Mongodb" --serviceDisplayName "Mongodb" --install

# import tesserocr
# import pymysql
# import
#
# from PIL import Image

# image = Image.open('image.png')
# #open image
#
# #print(image)
#
# print(tesserocr.image_to_text(image))

# from flask import Flask
# app=Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "HelloWorld"
#
# if __name__ == "__main__":
#     app.run()

# import tornado.ioloop
# import tornado.web
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("HelloWorld")
#
# def make_app():
#     return tornado.web.Application([
#         (r"/",MainHandler),
#     ])
#
# if __name__=="__main__":
#     app=make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()

# a='1234.jpg'
# print(list('1234'))

# import urllib.request
#
# response=urllib.request.urlopen('http://weixin.sogou.com/weixin')
# print(response.read())
# print(response.getheaders())

import requests

re=requests.get('http://weixin.sogou.com')
print(re.text)