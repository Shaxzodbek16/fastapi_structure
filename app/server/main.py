import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def get_ready() -> None:
    os.makedirs("media/", exist_ok=True)
    os.makedirs("static/", exist_ok=True)


def get_app() -> FastAPI:
    get_ready()
    app = FastAPI(
        title="API title",
        description="API description",
        version="API version",
    )
    # Tips: You can add routers here
    return app


def create_app() -> FastAPI:
    app: FastAPI = get_app()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
    return app
