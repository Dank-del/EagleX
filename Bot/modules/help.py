import asyncio
from pyrogram import filters
from Bot import app



mainhelptext = f"""
『 MAIN 』
  .adminhelp -> show help for admin stuff.
  .infohelp -> show help for info stuff.
  .devhelp -> show help for dev stuff.
  .mischelp -> show help for misc stuff.
"""

@app.on_message(filters.me & filters.regex("^\.help$"))
def mainhelp(_, m): 
    m.edit(mainhelptext)

adminhelptext = f"""
『 ADMIN STUFF 』
  .ban -> Bans user indefinitely.
  .unban -> Unbans the user.
  .mute -> Mutes user indefinitely.
  .unmute -> Unmutes the user.
  .kick -> Kicks the user out of the group.
  .pin -> pins a message.
  .del -> delete a message.
  .purge -> purge message(s)
"""

@app.on_message(filters.me & filters.regex("^\.adminhelp$"))
def adminhelp(_, m): 
    m.edit(adminhelptext)
    
infohelptext = f"""
『 INFO STUFF 』
  .whois -> get user info.
  .spb -> get info of a person from Intellivoid SpamProtection API.
"""

@app.on_message(filters.me & filters.regex("^\.infohelp$"))
def infohelp(_, m): 
    m.edit(infohelptext)    


devhelptext = f"""
『 DEV STUFF 』
  .eval -> evaluate python expressions.
  .term -> shell inside EagleX.
"""

@app.on_message(filters.me & filters.regex("^\.devhelp$"))
def devhelp(_, m): 
    m.edit(devhelptext)

mischelptext = f"""
『 MISC 』
  .paste -> paste text to nekobin.
  .tr (ang_code) -> translate text message.
"""
    
@app.on_message(filters.me & filters.regex("^\.mischelp$"))
def mischelp(_, m): 
    m.edit(mischelptext)
     
    
