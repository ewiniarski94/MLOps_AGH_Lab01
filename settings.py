# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        allowed_values = ("dev", "test", "prod")
        if value not in allowed_values:
            raise ValueError(f"Invalid environment: {value}.")
        return value
