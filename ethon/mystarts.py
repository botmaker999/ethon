from telethon import events, Button

async def start_srb(event, st):
    await event.reply(
        st,
        buttons=[
            [Button.inline("ꜱᴇᴛ ᴛʜᴜᴍʙ 🖼️", data="set"),
             Button.inline("ʀᴇᴍ ᴛʜᴜᴍʙ ✖️", data="rem")],         
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
