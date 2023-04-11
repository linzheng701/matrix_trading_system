import importlib
import time
from config import config
import matplotlib.pyplot as plt


def show_chart(data):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置全局字体为黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题

    x = data['所属行业']
    y = data['金额']
    plt.bar(x, y)

    plt.title('行业日成交量汇总')
    plt.xlabel('所属行业')
    plt.ylabel('金额（万元）')
    # 关闭y轴的科学计数法
    plt.ticklabel_format(style='plain', axis='y')

    # 设置 x 轴文字纵向排列
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
    # 记录开始时间
    start_time = time.time()

    file_name = "2023-04-10"

    processor_class = getattr(importlib.import_module(config.system_config.data_preprocessor_module),
                              config.system_config.data_preprocessor_class)
    processor = processor_class(file_name)
    df = processor.process()

    grouped = df.groupby('所属行业')
    result = grouped.agg({'金额': ['sum', 'count']}).sort_values(by=('金额', 'sum'), ascending=False)

    output_file_path = config.system_config.data_output + file_name + '.csv'
    result.to_csv(output_file_path, encoding='gbk')

    # 显示图表
    # show_chart(df)

    # 记录结束时间
    end_time = time.time()

    # 计算运行时间并输出
    run_time = end_time - start_time
    print(f"Program finished in {run_time:.2f} seconds.")
