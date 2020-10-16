import asyncio
from pyrogram import filters
from Bot import app

@app.on_message(filters.me & filters.regex("^\.alive$"))
def alive(_, m): 
   photo = "https://telegra.ph/file/bf51cb37c64037205d849.jpg"
   m.reply_photo(photo, caption='EagleX.\n Running on @Pyrogram 1.0.7\n Source: github.com/Dank-del/EagleX')