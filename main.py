import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def load_secrets(path: str = "secrets.yaml") -> None:
    with open(path, "r") as file:
        data = yaml.safe_load(file)
        if data:
            for key, value in data.items():
                os.environ[key] = str(value)


def export_envs(environment: str = "dev") -> None:
    env_path = os.path.join("config", f".env.{environment}")
    load_dotenv(dotenv_path=env_path, override=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    load_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
