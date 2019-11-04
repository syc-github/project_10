import pymysql
from config import *

connent = pymysql.connect(host=host,
                          user=user,
                          password=password,
                          port=port,
                          db=db)

cursor = connent.cursor()


#查询所有信息
def select_all():
    cursor.execute("select title,author,content from blogs")
    res = cursor.fetchall()
    return res


#增加信息
def add_info():
    cursor.execute("insert into blogs (title,author,content)value('学习使我快乐','张金涛','如果你隐约感觉有人不太喜欢你，不要怀疑，那个人在背后早就把你讨厌透顶了，甚至比你想象的恶毒一万倍，所以不要试图去友好，应该拿出冷漠的态度并且尽量远离。 如果你犹豫有些话该不该说，不要犹豫，千万不要说。你潜意识里觉得不该说的话，都是说了会产生不好的影响，会被人抓住话柄的。')")


add_info()


#删除信息
def del_info():
    cursor.execute("delete from blogs where title='小黄'")


#修改信息
def alter_info():
    pass




