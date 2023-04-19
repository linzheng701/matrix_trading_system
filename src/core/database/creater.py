from peewee import *

# 定义数据库连接
db = SqliteDatabase('my_database.db')


# 定义 Person 模型类
class Person(Model):
    name = CharField()
    age = IntegerField()
    gender = CharField()

    class Meta:
        database = db


# 连接数据库并创建表
db.connect()
db.create_tables([Person])
