import akshare as ak


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
    print(stock_profile_cninfo_df)
