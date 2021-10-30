from app.core import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_app() -> FastAPI:
    app = FastAPI(title=config.PROJECT_NAME, version=config.PROJECT_VERSION)

    app.add_middleware(CORSMiddleware,
                       allow_origins=['*'],
                       allow_credentials=True,
                       allow_methods=['*'],
                       allow_headers=['*'])

    return app


app = get_app()
