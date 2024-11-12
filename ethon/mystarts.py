from telethon import events, Button

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

@Drone.on(events.callbackquery.CallbackQuery(data="close"))
async def close(event):
    try:
        await event.message.delete()  # Delete bot's message
        reply_message = await event.get_reply_message()
        if reply_message:
            await reply_message.delete()  # Delete user's message if exists
    except Exception as e:
        print(f"Error in close: {e}")
