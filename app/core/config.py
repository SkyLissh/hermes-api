import os
from dotenv import load_dotenv
from typing import Union, Optional, Any, Mapping
from pydantic import BaseSettings, AnyHttpUrl, validator, PostgresDsn

load_dotenv()


class Settings(BaseSettings):
    API_VERSION: str = "/api/v1"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        'http://localhost:3000',
        'https://localhost:3000',
        'http://localhost'
    ]

    @classmethod
    @validator('BACKEND_CORS_ORIGIN', pre=True)
    def assemble_cors_origins(cls, v: Union[str, list[str]]) -> Union[list[str], str]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "Hermes API"

    SQLALCHEMY_DATABASE_URI = PostgresDsn.build(
            scheme='postgresql',
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('POSTGRES_SERVER'),
            path='/' + os.getenv('POSTGRES_DB'))

    @classmethod
    @validator('SQLALCHEMY_DATABASE_URI', pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Mapping[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme='postgresql',
            user=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASSWORD'),
            host=values.get('POSTGRES_SERVER'),
            path=f'/{values.get("POSTGRES_DB") or ""}'
        )

    class Config:
        case_sensitive = True


settings = Settings()
