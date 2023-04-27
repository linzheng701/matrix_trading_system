import importlib
import time
from core.database.creater import *
from util.bond_downloader import *
from config import config
import pandas as pd
import numpy as np


def get_base_volatility(code):
    # 读取股票数据
    stock_data = pd.read_csv(f'../data/raw/daily/{code}.csv')

    # 计算对数收益率
    returns = np.diff(stock_data['收盘']) / stock_data['收盘'][:-1]

    # 计算股票波动率(放大100倍)
    volatility = np.sqrt(252) * np.std(returns) * 100

    print(code, '波动率为:', round(volatility, 2))


def statistics_industry_vol():
    file_name = time.strftime("%Y-%m-%d", time.localtime())

    # load config module
    processor_class = getattr(importlib.import_module(config.system_config.data_preprocessor_module),
                              config.system_config.data_preprocessor_class)
    processor = processor_class(file_name)
    df = processor.process()

    grouped = df.groupby('所属行业')
    result = grouped.agg({'金额': ['sum', 'count']}).sort_values(by=('金额', 'sum'), ascending=False)
    result.columns = ['总成交量（万元）', '该行业股票个数']
    result['平均成交量（万元）'] = result['总成交量（万元）'] / result['该行业股票个数']

    # data format
    result['总成交量（万元）'] = result['总成交量（万元）'].round(0)
    result['平均成交量（万元）'] = result['平均成交量（万元）'].round(0)

    output_file_path = config.system_config.data_output + file_name + '.csv'
    result.to_csv(output_file_path, encoding='gbk')


def calc_beta(data_benchmark, data_comparison, period=252):
    # data_benchmark表示基准股票的历史价格数据，data_comparison表示需要对照股票的历史价格数据

    if len(data_benchmark) < period or len(data_comparison) < period:
        print("period is to long")
        return

    # 计算基准和对照的收益率
    benchmark = data_benchmark[0:period].pct_change()
    comparison = data_comparison[0:period].pct_change()
    benchmark = np.nan_to_num(benchmark, nan=0)
    comparison = np.nan_to_num(comparison, nan=0)

    # 计算基准和对照的收益率之间的协方差和对照的收益率的方差
    covariance = np.cov(benchmark, comparison)[0][1]
    variance_b = np.var(comparison)

    # 计算beta值
    beta = covariance / variance_b

    print("Beta值为：", beta)


def test():
    # 记录开始时间
    start_time = time.time()

    get_base_volatility("399300")

    get_base_volatility("000002")
    get_base_volatility("002174")
    get_base_volatility("300033")
    get_base_volatility("300122")
    get_base_volatility("300759")
    get_base_volatility("601872")
    get_base_volatility("603776")
    get_base_volatility("601398")

    # 记录结束时间
    end_time = time.time()

    # 计算运行时间并输出
    run_time = end_time - start_time
    print(f"Program finished in {run_time:.2f} seconds.")


if __name__ == '__main__':
    # create_tables()
    bond_realtime_info()
    # statistics_industry_vol()
    # get_stock_realtime_info()
    # get_stock_profile('000001')
    # get_hs300_stock_list()
    # 沪深300为基准
    # stock_benchmark = pd.read_csv(f'../data/raw/daily/399300.csv')
    # stock_data = pd.read_csv(f'../data/raw/daily/002174.csv')
    # calc_beta(stock_benchmark['收盘'], stock_data['收盘'])
