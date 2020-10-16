import asyncio
import importlib
import sys
import time
import traceback
import logging
from pyrogram import  idle, Client
from Bot import app
from Bot.modules import alive, admin, pin, whois


app.start()
idle()