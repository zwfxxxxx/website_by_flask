import yaml


def get_config():
    # 读取yaml配置文件
    with open('config/config.yaml', 'r', encoding='utf-8') as f:
        _config = yaml.load(f, Loader=yaml.FullLoader)
    return _config


config = get_config()
