from telethon import events, Button

API_ID = 17822592
API_HASH = "a20b3dbbe07ed695563b4609a3e62012"
BOT_TOKEN = "7576139299:AAGIS053Y3KbRgFPog9tRcpiNSnYD9c8wxE"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

async def start_srb(event, st):
    await event.reply(
        st,
        buttons=[
            [Button.inline("ꜱᴇᴛ ᴛʜᴜᴍʙ 🖼️", data="set"),
             Button.inline("ʀᴇᴍ ᴛʜᴜᴍʙ ✖️", data="rem")],
            [Button.inline("ᴄʟᴏꜱᴇ", data="close")]
        ]
    )

async def vc_menu(event):
    await event.edit(
        "**VIDEO CONVERTOR v1.4**",
        buttons=[
            [Button.inline("info.", data="info"),
             Button.inline("SOURCE", data="source")],
            [Button.inline("NOTICE.", data="notice"),
             Button.inline("Main.", data="help")],
            [Button.inline("ᴄʟᴏꜱᴇ", data="close")],  # Added the close button here
            [Button.url("DEVELOPER", url="t.me/MaheshChauhan")]
        ]
    )

@bot.on(events.callbackquery.CallbackQuery(data="close"))
async def close(event):
    try:
        await event.message.delete()  # Delete bot's message
        reply_message = await event.get_reply_message()
        if reply_message:
            await reply_message.delete()  # Delete user's message if exists
    except Exception as e:
        print(f"Error in close: {e}")
