from typing import Any, Dict

from pydantic_settings import BaseSettings


class CommonSettings(BaseSettings):
    API_V1: str = "/v1"
    ROOT_PATH: str = "/api"
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    debug: bool = True
    title: str = "FastAPI backend application"
    version: str = "0.3.0b"
    openapi_url: str = "/openapi.json"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_prefix: str = ""

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "title": self.title,
            "version": self.version,
            "openapi_url": self.openapi_url,
            "docs_url": self.docs_url,
            "redoc_url": self.redoc_url,
            # "root_path": self.ROOT_PATH,
            "openapi_prefix": self.openapi_prefix,
        }
