from dataclasses import dataclass


@dataclass
class Daily:
    # 代码
    code: str
    # 名称
    name: str
    # 开盘价
    open: float
    # 收盘价
    close: float
    # 最高价
    high: float
    # 最低价
    low: float
    # 涨跌幅（%）
    change: float
    # 成交量（万）
    volume: float
    # 所属行业
    industry: str
    # 总市值
    market_capitalization: float
    # 流通市值
    free_float_market_capitalization: float
    # 市净率
    pb: float
