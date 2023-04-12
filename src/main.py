import importlib
import time
from config import config

if __name__ == '__main__':
    # 记录开始时间
    start_time = time.time()

    file_name = "2023-04-12"

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

    # 记录结束时间
    end_time = time.time()

    # 计算运行时间并输出
    run_time = end_time - start_time
    print(f"Program finished in {run_time:.2f} seconds.")
