from peewee import *
import os

current_path = os.getcwd()
print(current_path)

# 定义数据库连接
db = SqliteDatabase('../data/db/base')
# 连接数据库
db.connect()


# 公司概况
class StockProfileInfo(Model):
    companyName = CharField()
    englishName = CharField()
    usedName = CharField()
    code = CharField()
    name = CharField()
    bCode = CharField()
    bShortName = CharField()
    hCode = CharField()
    hShortName = CharField()
    indexInclusion = CharField()
    market = CharField()
    industry = CharField()
    lr = CharField()  # 法人代表
    registeredCapital = CharField()
    dataOfEstablishment = CharField()
    listingData = CharField()
    website = CharField()
    email = CharField()
    tel = CharField()
    fax = CharField()
    registeredAddress = CharField()
    officeAddress = CharField()
    postalCode = CharField()
    mainBusiness = CharField()
    businessScope = CharField()
    introduction = CharField()

    class Meta:
        database = db


def dataframe_to_models(df, model_class):
    return [model_class(**row) for row in df.to_dict(orient='records')]


def create_tables():
    db.create_tables([StockProfileInfo])
