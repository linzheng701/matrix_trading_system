import os
from src.core.preprocessor.BaseProcessor import BaseProcessor
from src.config import config
from src.util.files import load_excel, load_csv


# 东方财富日线Excel数据处理程序
class EastMoneyTableProcessor(BaseProcessor):
    def __init__(self, file_name):
        self.file_name = file_name

    def process(self):
        # 文件已清洗，退出处理程序
        clean_file_path = config.system_config.data_processed + self.file_name + '.csv'
        if os.path.exists(clean_file_path):
            return load_csv(clean_file_path)

        raw_file_path = config.system_config.data_raw + self.file_name + '.xlsx'
        df = load_excel(raw_file_path, 'Table')

        # 亿转换成万
        contains_yi = df['金额'].str.contains('亿')
        # 万去除中文
        contains_wang = df['金额'].str.contains('万')
        # 空字段替换为零
        contains_empty = df['金额'].str.contains('—')

        contains_yi = contains_yi.fillna(method='ffill')
        contains_wang = contains_wang.fillna(method='ffill')
        contains_empty = contains_empty.fillna(method='ffill')

        # 替换
        df.loc[contains_empty, '金额'] = 0.0
        df.loc[contains_yi, '金额'] = df.loc[contains_yi, '金额'].str.replace('亿', '').astype(float) * 10000
        df.loc[contains_wang, '金额'] = df.loc[contains_wang, '金额'].str.replace('万', '').astype(
            float) * 1.0
        df.to_csv(clean_file_path, index=False, encoding='gbk')

        return df
