from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret

config = Config("./.env")

PROJECT_NAME = config("PROJECT_NAME", cast=str)
PROJECT_VERSION = config("PROJECT_VERSION", cast=str)

SECRET_KEY = config("SECRET_KEY", cast=Secret)
POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str)
POSTGRES_PORT = config("POSTGRES_PORT", cast=str)
POSTGRES_DB = config("POSTGRES_DB", cast=str)

DATABASE_URL = config(
    "DATABASE_URL",
    cast=DatabaseURL,
    default=
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
