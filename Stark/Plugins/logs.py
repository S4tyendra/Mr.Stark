import os
from pyrogram import Client, filters

@Client.on_message(filters.command(["log", "logs"]))
async def log_cmd(bot, message):
    processing = await message.reply_text("Processing")
    if os.path.exists("log.txt"):
        await message.reply_document("log.txt",caption="__**Logs of Mr.Stark**__")
        await processing.delete()
    else:
        await processing.edit("`File not found`")