#main.py

from fastapi import FastAPI
from core.config import settings
from apis.base import api_router

def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
    include_router(app)
    #create_tables()
    return app

app=start_application()

@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI🚀"}