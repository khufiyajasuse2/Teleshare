import logging
import sys
from pathlib import Path
from typing import List

from pydantic import BaseSettings, validator, ValidationError
from pydantic_settings import SettingsConfigDict

BASE_PATH = Path(__file__).parent.parent

class Config(BaseSettings):
    PORT: int = 8080
    HOSTNAME: str = "0.0.0.0"
    HTTP_SERVER: bool = True

    API_ID: int = 27573283
    API_HASH: str = "eca55c9f1b0a14260e0ee1978aa17b2b"
    BOT_TOKEN: str = "7297125221:AAF_hS-k7BSBaUDY0f9fL0j54XZdKWfFACQ"
    BOT_WORKER: int = 8
    BOT_SESSION: str = "Ayesha121_bot"
    BOT_MAX_MESSAGE_CACHE_SIZE: int = 1250

    MONGO_DB_URL: str = "mongodb+srv://ashwinimalaysian:5gRvQgPW4DRhlEpE@pehla.uuzwevb.mongodb.net/?retryWrites=true&w=majority&appName=pehla"
    MONGO_DB_NAME: str = "pehla"

    RATE_LIMITER: bool = True
    BACKUP_CHANNEL: int = -1002202226579

    # Updated values with comma-separated strings for lists
    ROOT_ADMINS_ID: List[int] = [6371924437]  # Single value in a list
    PRIVATE_REQUEST: bool = False
    PROTECT_CONTENT: bool = True
    FORCE_SUB_CHANNELS: List[int] = [-1002233922329]  # Single value in a list
    AUTO_GENERATE_LINK: bool = True

    model_config = SettingsConfigDict(
        env_file=f"{BASE_PATH}/.env",
    )

    @validator('ROOT_ADMINS_ID', 'FORCE_SUB_CHANNELS', pre=True, each_item=True)
    def parse_list(cls, v):
        if isinstance(v, str):
            # Convert comma-separated string to list of integers
            return [int(x) for x in v.split(',') if x]
        return v

try:
    config = Config()  # type: ignore[reportCallIssue]
except (ValidationError, SettingsError) as e:
    logging.exception("Configuration Error: %s", e)
    sys.exit(1)
