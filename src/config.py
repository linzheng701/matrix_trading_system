import json
from models.system_config import SystemConfig, DailyConfig


class Config:
    def __init__(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            config_file = json.load(file)
            self.system_config = SystemConfig(**config_file['system'])
            self.daily_config = DailyConfig(**config_file['daily'])


# 全局配置文件
config = Config('config/config.json')
