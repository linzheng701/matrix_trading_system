from dataclasses import dataclass


@dataclass
class SystemConfig:
    data_output: str
    data_processed: str
    data_raw: str
    data_preprocessor_module: str
    data_preprocessor_class: str


@dataclass
class DailyConfig:
    code: str
    name: str
    open: str
    close: str
    high: str
    low: str
    change: str
    volume: str
    industry: str
    market_capitalization: str
    free_float_market_capitalization: str
    pb: str
