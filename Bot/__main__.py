from pyrogram import idle, Client
from Bot import app
from Bot.modules import (
    alive,
    admin,
    pin,
    whois,
    dev,
    help,
    ping,
    paste,
    purge,
    spb,
    translate,
)


app.start()
idle()
