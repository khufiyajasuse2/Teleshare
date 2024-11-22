"""General configuration.

Config: Bot Config
"""

# ruff: noqa: ARG003
import logging
import sys
from pathlib import Path
from typing import Annotated

from pydantic import ValidationError
from pydantic.networks import UrlConstraints
from pydantic_core import MultiHostUrl
from pydantic_settings import (
    BaseSettings,
    DotEnvSettingsSource,
    EnvSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)
from pydantic_settings.sources import SettingsError

MongoSRVDsn = Annotated[MultiHostUrl, UrlConstraints(allowed_schemes=["mongodb+srv"])]
BASE_PATH = Path(__file__).parent.parent


class Config(BaseSettings):
    """A general configuration setup to read either .env or environment keys."""

    # Bot deploy config
    PORT: int = 8080
    HOSTNAME: str = "0.0.0.0"  # noqa: S104
    HTTP_SERVER: bool = True

    API_ID: 27573283
    API_HASH: eca55c9f1b0a14260e0ee1978aa17b2b
    BOT_TOKEN: 
    BOT_WORKER: int = 8
    BOT_SESSION: str = "@Sumairakhan_bot"
    BOT_MAX_MESSAGE_CACHE_SIZE: int = 1250

    MONGO_DB_URL: mongodb+srv://sumairakhan122112:fqkbPZBYIADqX1fk@terabox.cv45syt.mongodb.net/?retryWrites=true&w=majority&appName=terabox
    MONGO_DB_NAME: str = "pehla"

    # Bot main config
    RATE_LIMITER: bool = True
    BACKUP_CHANNEL: -1002413901220
    ROOT_ADMINS_ID: list[int] = [6371924437]
    PRIVATE_REQUEST: bool = False
    PROTECT_CONTENT: bool = True 
    FORCE_SUB_CHANNELS: list[int] = [-1002368840069]
    AUTO_GENERATE_LINK: bool = True

    model_config = SettingsConfigDict(
        env_file=f"{BASE_PATH}/.env",
    )
from pydantic import BaseSettings, validator
from typing import List

    @classmethod
    def settings_customise_sources(  # noqa: PLR0913
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            DotEnvSettingsSource(settings_cls),
            EnvSettingsSource(settings_cls),
        )


try:
    config = Config()  # type: ignore[reportCallIssue]
except (ValidationError, SettingsError):
    logging.exception("Configuration Error")
    sys.exit(1)
