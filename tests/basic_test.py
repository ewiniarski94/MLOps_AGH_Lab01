from fastapi.testclient import TestClient
from main import export_envs
from app import app
from settings import Settings

export_envs("test")

client = TestClient(app)


def test_settings_are_test_specific():
    export_envs("test")
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "lab01"
    assert settings.API_KEY == "test_key"


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_welcome_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}
