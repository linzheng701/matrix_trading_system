import importlib
import time
import os
from config import config
import pandas as pd
import numpy as np


def get_base_volatility(code):
    # 读取股票数据
    stock_data = pd.read_csv(f'../data/raw/daily/{code}.csv')

    # 计算对数收益率
    stock_data['log_return'] = np.log(stock_data['收盘']) - np.log(stock_data['收盘'].shift(1))

    # 计算股票波动率(放大100倍)
    volatility = np.sqrt(252) * np.std(stock_data['log_return']) * 100

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
    statistics_industry_vol()
