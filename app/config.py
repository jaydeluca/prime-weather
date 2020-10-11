import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    def __init__(self):
        pass

    CONFIG_NAME = "base"
    DEBUG = False
    SERVICE_NAME = os.getenv("SERVICE_NAME")
    SECRET_TOKEN = os.getenv("SECRET_TOKEN")
    API_KEY = os.getenv("API_KEY")
    JSON_LOGGING = os.getenv("JSON_LOGGING") if os.getenv("JSON_LOGGING") is not None else False


class DevConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    WEATHER_API_KEY = os.getenv("DEV_WEATHER_API_KEY")


class TestConfig(BaseConfig):
    CONFIG_NAME = "test"
    WEATHER_API_KEY = os.getenv("TEST_WEATHER_API_KEY")


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevConfig,
    TestConfig
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}