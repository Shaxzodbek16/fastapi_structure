from fastapi import FastAPI
from app.api.routers.test import router as test_router

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(test_router)
    return app
