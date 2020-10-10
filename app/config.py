import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    def __init__(self):
        pass

    CONFIG_NAME = "base"
    DEBUG = False


class DevConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    API_KEY = os.getenv("DEV_SECRET_KEY")


class TestConfig(BaseConfig):
    CONFIG_NAME = "test"
    API_KEY = os.getenv("TEST_SECRET_KEY")


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevConfig,
    TestConfig
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}