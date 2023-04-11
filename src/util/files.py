import pandas as pd


def load_excel(file_name, sheet_name='Sheet1'):
    return pd.read_excel(file_name, sheet_name=sheet_name)


def load_csv(file_name):
    return pd.read_csv(file_name, encoding='gbk')
