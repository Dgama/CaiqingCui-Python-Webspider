import requests
from  pyquery import PyQuery as pq
import json
import csv
import pymysql
import pymongo
from bson import ObjectId
from  redis import StrictRedis
#
# url='https://www.zhihu.com/explore'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like'
#                  ' Gecko) Chrome/73.0.3683.103 Safari/537.36',}
# html=requests.get(url,headers=headers).text
# doc=pq(html)
# items = doc('.explore-tab .feed-item').items()
#
# for item in items:
#     question=item.find('h2').text()
#     author=item.find('.author-link-line').text()
#     answer=pq(item.find('.content').html()).text()
#     file= open('explore.txt','a',encoding='utf-8')
#     file.write('\n'.join([question,author,answer]))
#     file.close()

# str='''
# [{"name":"好","age":"22"},{"name":"will","age":"21"}]
# '''
#
# print(type(str))
# data=json.loads(str)
# print(data)
# print(type(data))
# print(data[0]['name'])
# print(data[0].get('hhh'))
#
# with open('data.json','w') as file:
#     file.write(json.dumps(data,indent=2,ensure_ascii=False))

# with open('data.csv','w') as file:
#     writer= csv.writer(file,delimiter=' ')
#     writer.writerow(['id','name','age'])
#     writer.writerows([['10001', 'hhh', '21'],['10001', 'hhh', '21']])
#     writer.writerow({'10001', 'hhh', '21'})

# with open('data.csv','w',encoding='utf-8') as file:
#     header=['id','name']
#     writer=csv.DictWriter(file,fieldnames=header)
#     writer.writeheader()
#     writer.writerow({'id':1,'name':'goood'})

# with open('data.csv','r',encoding='utf-8') as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)

# db=pymysql.connect(host='localhost',user='root',password='root',port=3306)
# cursor=db.cursor()
# cursor.execute('SELECT VERSION()')
# data=cursor.fetchone()
# print('Database Version:',data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

# db=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')
# cursor=db.cursor()
# sql=' CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL , name VARCHAR(255) NOT NULL , age INT NOT NULL,PRIMARY KEY(id))'
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

# id='20120001'
# user='Bob'
# age=20
#
# sql_two='INSERT INTO students(id, name, age) values(%s,%s,%' \
#         '333333s)'
# try:
#     cursor.execute(sql_two,(id,user,age))
#     db.commit()
# except:
#     print('error occured')
#     db.rollback()
# db.close()

# db=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')
# cursor=db.cursor()
# data={
#     'id':'100001',
#     'name':'Bob',
#     'age':21
# }
# table='students'
# keys=','.join(data.keys())
# values=','.join(['%s']*len(data))
# sql='INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE '.format(table=table,keys=keys,values=values)
# update=','.join(["{key}=%s".format(key=key) for key in data])
# sql+=update
# try:
#     cursor.execute(sql,tuple(data.values())*2)
#     db.commit()
# except:
#     db.rollback()
#     print('failed')
# db.close()

# client=pymongo.MongoClient(host='localhost',port=27017)
# db=client.test
# collection=db.students
# students1={
#     'id':'20170101',
#     'name':'Jordan',
#     'age':20,
#     'gender':'male'
# }
# students2={
#     'id':'20170102',
#     'name':'Jordan2',
#     'age':21,
#     'gender':'female'
# }
# result=collection.insert_many([students1,students2])
# print(result)

# result=collection.find_one({'name':'Jordan'})
# print(type(result))
# print(result)
# result=collection.find_one({'_id':ObjectId('5cc2c32efb6559024c6c2cba')})
# students1['age']=26
# result=collection.update_one({'_id':ObjectId('5cc2c32efb6559024c6c2cba')},{'$set':students1})
# print(result)
# print(result.matched_count,result.modified_count)
# results=collection.find({'gender':{'$regex':'^m.*'}})
# print(results.count())
# for result in results:
#     print(result)


# redis=StrictRedis(host='localhost',port=6379,db=0)
# redis.set('name','Bob')
# print(redis.get('name'))