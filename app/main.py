from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import find_dotenv, load_dotenv

from app.api.api_v1.api import api_router
from app.core.config import settings

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app: FastAPI = FastAPI(title=settings.PROJECT_NAME, openapi_url=f'{settings.API_VERSION}/openapi.json')

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

app.include_router(api_router, prefix=settings.API_VERSION)
