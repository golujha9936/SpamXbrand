from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_BUTTON = [
    [Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/About_Aryan_Owner/3"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/Ace_networkop")
    ],
    [Button.url("• Oᴡɴᴇʀ •", "https://t.me/FAKE_ARYAN")]
]

# Define a list of handlers
handlers = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Register event handlers
for handler in handlers:
    @handler.on(events.NewMessage(pattern="/start"))
    async def start(event):
        if event.is_private:
            ANNIE = await event.client.get_me()
            bot_name = ANNIE.first_name
            bot_id = ANNIE.id

            TEXT = (
                f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n"
                f"ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n━━━━━━━━━━━━━━━━━━━\n\n"
                f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [Evo^xᴅ 𓆩🇮🇳𓆪 ](https://t.me/EvoXpro)\n\n"
                f"» **ᴊᴀʀᴠɪs V2 :** `M 1.8.31`\n"
                f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
                f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
            )

            await event.client.send_file(
                event.chat_id,
                "https://graph.org/file/6519b78c59d6d5df56a85.jpg",
                caption=TEXT,
                buttons=START_BUTTON
            )
