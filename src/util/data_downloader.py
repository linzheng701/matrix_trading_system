import akshare as ak
from src.core.database.creater import *


def get_hs300_stock_list():
    index_stock_cons_df = ak.index_stock_cons(symbol="399300")
    print(index_stock_cons_df)


def get_stock_realtime_info():
    stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
    stock_zh_a_spot_em_df.to_csv('D:/1.csv', index=False, encoding='gbk')
    print('接收实时数据完成')


def get_stock_history_info(symbol, end_date):
    # 前复权的日线数据
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date="20200101", end_date=end_date,
                                            adjust="qfq")
    print(stock_zh_a_hist_df)


def get_stock_profile(symbol):
    stock_profile_cninfo_df = ak.stock_profile_cninfo(symbol=symbol)
    stock_profile_cninfo_df = stock_profile_cninfo_df.rename(columns={
        '公司名称': 'companyName', '英文名称': 'englishName', '曾用简称': 'usedName', 'A股代码': 'code',
        'A股简称': 'name', 'B股代码': 'bCode', 'B股简称': 'bShortName', 'H股代码': 'hCode',
        'H股简称': 'hShortName', '入选指数': 'indexInclusion', '所属市场': 'market', '所属行业': 'industry',
        '法人代表': 'lr', '注册资金': 'registeredCapital', '成立日期': 'dataOfEstablishment', '上市日期': 'listingData',
        '官方网站': 'website', '电子邮箱': 'email', '联系电话': 'tel', '传真': 'fax',
        '注册地址': 'registeredAddress', '办公地址': 'officeAddress', '邮政编码': 'postalCode',
        '主营业务': 'mainBusiness',
        '经营范围': 'businessScope', '机构简介': 'introduction'
    })
    stock_profile_cninfo_df.fillna("", inplace=True)
    info = dataframe_to_models(stock_profile_cninfo_df, StockProfileInfo)
    with db.atomic():
        StockProfileInfo.bulk_create(info)
    print("下载基础数据完成")
