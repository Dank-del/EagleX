import logging
import sys
from pyrogram import Client, errors
from Bot.config import Config


API_ID = Config.API_ID
API_HASH = Config.API_HASH
SESSION = Config.SESSION

app = Client(SESSION, api_id=API_ID, api_hash=API_HASH)