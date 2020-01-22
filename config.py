import os


class Config:
    PG_USER = "andrew_lee"
    PG_PASSWORD = "password"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "store_db"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class TestConfig(Config):
    TEST_VALUE = "TEST_CONFIG_VALUE"
    DEBUG = True


class ProdConfig(Config):
    TEST_VALUE = "PROD_CONFIG_VALUE"
    DEBUG = False


def run_config():
    env = os.environ.get("ENV")
    config = {"TEST": TestConfig, "PROD": ProdConfig}
    return config.get(env, Config)
