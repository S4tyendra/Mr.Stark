import os
import openai
import requests
from pyrogram import Client, filters
from Stark import error_handler

openai.api_key = "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"


@Client.on_message(filters.command(["generate", "genimage"]))
@error_handler
async def ai_image(bot, message):
    x = await message.reply_text("`Generating images, it may take a while`")
    try:
        text = message.text.split(None, 1)[1]
    except:
        await message.reply_text(
            "`ɪ ᴅɪᴅɴ'ᴛ ɢᴇᴛ ᴛʜᴀᴛ`"
        )
        return
    response = openai.Image.create(
        prompt=text,
        n=3
    )
    for i in range(3):
        try:
            image_url = response['data'][i]['url']
            await message.reply_photo(image_url)
        except:
            await x.edit("`Something unexpected happened`")
            quit()
    await x.delete()
