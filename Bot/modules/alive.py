import asyncio
import time
from pyrogram import filters
from Bot import app, StartTime
from sys import version_info

from pyrogram import __version__ as __pyro_version__  # noqa

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

start_time = time.time()
uptime = get_readable_time((time.time() - StartTime))
end_time = time.time()
ping_time = round((end_time - start_time) * 1000, 3)

output = f"""
**EagleX.**
**Uptime** : `{uptime}`
**Ping**: `{ping_time}ms`
    **Python**: `{__python_version__}`
    **@Pyrogram**: `{__pyro_version__}`
    **Source**: github.com/Dank-del/EagleX 
"""

@app.on_message(filters.me & filters.regex("^\.alive$"))
def alive(_, m): 
   photo = "https://telegra.ph/file/bf51cb37c64037205d849.jpg"
   m.reply_photo(photo, caption=output)