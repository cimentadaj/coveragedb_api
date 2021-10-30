from starlette.config import Config

config = Config("./.env")

PROJECT_NAME = config("PROJECT_NAME", cast=str)
PROJECT_VERSION = config("PROJECT_VERSION", cast=str)
