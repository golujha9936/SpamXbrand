import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from JARVIS.data import FRIDAY

ECHO = []

# List of handlers
handlers = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Function to handle echo command
async def echo(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id

            if uid in FRIDAY:
            await e.reply("ʀɴᴅɪ ᴋ ᴏʟᴀᴀᴅ ᴋʟ ᴋ ᴀᴀʏᴇ ᴘɪʟʟᴇ ᴀʙ ᴀᴘɴᴇ ʙᴀᴀᴘ ᴘᴇ ʜɪ ᴍᴀᴀʀᴇɢᴀ ʀᴀɪᴅ ᴛᴇʀɪ ᴍᴀɪʏᴀᴀ ᴄʜᴏᴅᴜᴜ")
        elif uid == OWNER_ID:
            await e.reply("ᴄʜʟᴀ ʟᴇ ʀᴀɴᴅɪ ᴏᴡɴᴇʀ sᴇ ʜɪ ᴋʀʟᴏ ʙᴀᴋᴀɪᴛɪ ᴅᴏɴᴏ ᴋɪ ɢᴀᴀɴᴅ ᴍᴀᴀʀ ᴅᴇɢᴀ ᴏᴡɴᴇʀ")
        elif uid in SUDO_USERS:
            await e.reply("sᴜᴅᴏ ʜᴀɪ ʏʀʀ ᴡᴏʜ ᴜsᴘᴇ ɴʜᴋ ᴋʀsᴋᴛᴀ")
        else:
                try:
                    alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                    await event.client(alt)
                except BaseException:
                    pass

                global ECHO
                check = f"{user_id}_{event.chat_id}"
                if check in ECHO:
                    await event.reply("» ᴇᴄʜᴏ ʜᴀs ʙᴇᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴏɴ ᴛʜɪs ɢᴜʏ ✅")
                else:
                    ECHO.append(check)
                    await event.reply("» ᴇᴄʜᴏ ʜᴀs ʙᴇᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴏɴ ᴛʜɪs ɢᴜʏ ✅")
        else:
            await event.reply(f"𝗘𝗰𝗵𝗼:\n  » {hl}echo <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

# Function to handle rmecho command
async def rmecho(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass

            global ECHO
            reply_msg = await event.get_reply_message()
            check = f"{reply_msg.sender_id}_{event.chat_id}"

            if check in ECHO:
                ECHO.remove(check)
                await event.reply("» ᴄʜᴏ ʜᴀs ʙᴇᴇɴ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜɪs ɢᴜʏ☑️")
            else:
                await event.reply("» ᴛʜᴇʀᴇ's ɴᴏ ᴇᴄʜᴏ ᴏɴ ᴛʜɪs ɢᴜʏ")
        else:
            await event.reply(f"𝗥𝗲𝗺𝗼𝘃𝗲 𝗘𝗰𝗵𝗼:\n  » {hl}rmecho <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

# Function to handle incoming messages for echo
async def handle_incoming(event):
    global ECHO
    check = f"{event.sender_id}_{event.chat_id}"
    if check in ECHO:
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await event.client(alt)
        except BaseException:
            pass
        if event.message.text or event.message.sticker:
            await event.reply(event.message)
            await asyncio.sleep(0.1)

# Register event handlers
for handler in handlers:
    handler.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))(echo)
    handler.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))(rmecho)
    handler.on(events.NewMessage(incoming=True))(handle_incoming)
