import asyncio
from pyrogram import filters
from Bot import app



mainhelptext = f"""
// MAIN //
.adminhelp -> show help for admin stuff.
.infohelp -> show help for info stuff.
.devhelp -> show help for dev stuff.
"""

@app.on_message(filters.me & filters.regex("^\.help$"))
def mainhelp(_, m): 
    photo = "https://telegra.ph/file/bf51cb37c64037205d849.jpg"
    m.reply_photo(photo, caption = mainhelptext)

adminhelptext = f"""
// ADMIN STUFF //
.ban -> Bans user indefinitely.
.ban 24 -> Bans user for 24hrs.,
.unban -> Unbans the user.
.mute -> Mutes user indefinitely.
.mute 24 -> Bans user for 24hrs.
.unmute -> Unmutes the user.
.kick -> Kicks the user out of the group.
.pin -> pins a message
"""

@app.on_message(filters.me & filters.regex("^\.adminhelp$"))
def adminhelp(_, m): 
    photo = "https://telegra.ph/file/bf51cb37c64037205d849.jpg"
    m.reply_photo(photo, caption = adminhelptext)
    
infohelptext = f"""
// INFO STUFF //
.whois -> get user info.
"""

@app.on_message(filters.me & filters.regex("^\.infohelp$"))
def infohelp(_, m): 
    photo = "https://telegra.ph/file/bf51cb37c64037205d849.jpg"
    m.reply_photo(photo, caption = infohelptext)    


devhelptext = f"""
// DEV STUFF //
.eval -> evaluate python expressions.
.term -> shell inside EagleX.
"""

@app.on_message(filters.me & filters.regex("^\.devhelp$"))
def devhelp(_, m): 
    photo = "https://telegra.ph/file/bf51cb37c64037205d849.jpg"
    m.reply_photo(photo, caption = devhelptext)
    
    
