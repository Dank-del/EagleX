import logging
import sys
import time
from pyrogram import Client, errors
from Bot.config import Config
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


StartTime = time.time()

API_ID = Config.API_ID
API_HASH = Config.API_HASH
SESSION = Config.SESSION

app = Client(SESSION, api_id=API_ID, api_hash=API_HASH)