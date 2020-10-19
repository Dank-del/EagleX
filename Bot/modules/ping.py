from datetime import datetime
from Bot import app
from pyrogram.types import Message
from pyrogram import filters


@app.on_message(filters.command("ping", ".") & filters.me)
async def pingme(_, message: Message):
    start = datetime.now()
    await message.edit("`Pong!`")
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**Pong!**\n`{m_s} ms`")
