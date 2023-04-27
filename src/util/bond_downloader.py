import akshare as ak
from src.core.database.creater import *


def bond_realtime_info():
    bond_zh_hs_cov_spot_df = ak.bond_zh_hs_cov_spot()
    bonds = dataframe_to_models(bond_zh_hs_cov_spot_df, StockProfileInfo)
    with db.atomic():
        BondReadtimeInfo.delete().execute()  # 清空表
        BondReadtimeInfo.bulk_create(bonds)
    print("实时数据更新完成")


def bond_daily(symbol):
    bond_zh_hs_cov_daily_df = ak.bond_zh_hs_cov_daily(symbol=symbol)
    print(bond_zh_hs_cov_daily_df)


def update_bond_daily():
    query = BondReadtimeInfo.select()
    for record in query:
        print(f"正在更新:{record.symbol}")
        bond_zh_hs_cov_daily_df = ak.bond_zh_hs_cov_daily(symbol=record.symbol)
        bonds = dataframe_to_models(bond_zh_hs_cov_daily_df, BondDaily)
        bonds['symbol'] = record.symbol
        bonds['code'] = record.code
        with db.atomic():
            BondDaily.bulk_create(bonds)
