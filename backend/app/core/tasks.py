import logging
from typing import Callable

from app.core.config import DATABASE_URL
from databases import Database
from fastapi import FastAPI

logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI):
    database = Database(DATABASE_URL, min_size=2, max_size=10)

    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn(" ---- DB CONNECTION ERROR ----")
        logger.warn(e)
        logger.warn(" ---- DB CONNECTION ERROR ----")


async def close_db_connection(app: FastAPI):
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn(" ---- DB DISCONNECTION ERROR ----")
        logger.warn(e)
        logger.warn(" ---- DB DISCONNECTION ERROR ----")


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app
