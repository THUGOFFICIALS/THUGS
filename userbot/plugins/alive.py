import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"
PM_IMG = "https://telegra.ph/file/f34675b4e94d4290c0b6b.mp4"
pm_caption = "🔥🔥**Hêllẞø† IS ONLINE🔥🔥\n\n\n"

pm_caption += f"**MASTER**       : {DEFAULTUSER}\n\n"

pm_caption += "🤖🤖**THUGBOT**🤖🤖        : __0.01__\n\n"

pm_caption += "⚠️⚠️**CHANNEL**⚠️⚠️       : [JOIN](https://t.me/THUG_UPDATE)\n\n"

pm_caption += "🏢🏢**SUPPORT**🏢🏢.       : [JOIN](https://t.me/THUG_SUPPORT)\n\n"

pm_caption += "👼👼GOD👼👼              : [THUG](https://t.me/brokendeadskull)\n\n"

pm_caption += "[┈┈┈┈┈┈▕▔╲┈┈┈┈┈┈\n┈┈┈┈┈┈┈▏▕┈THUGS\n┈┈┈┈┈┈┈▏▕▂▂▂┈┈┈\n▂▂▂▂▂▂╱┈▕▂▂▂▏┈┈\n▉▉▉▉▉┈┈┈▕▂▂▂▏┈┈\n▉▉▉▉▉┈┈┈▕▂▂▂▏┈┈\n▔▔▔▔▔▔╲▂▕▂▂▂▏┈┈\n](https://t.me/thugs_support)\n\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
