import os

import yaml


def get_config():
    # 读取yaml配置文件
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'config.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        _config = yaml.load(f, Loader=yaml.FullLoader)
    return _config


config = get_config()
