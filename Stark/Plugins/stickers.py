import os
import pyrogram
from pyrogram import enums
from pyrogram import Client, filters
from pyrogram.raw import types, functions

from Stark import error_handler
from main.helper_func.stcr_funcs import kangani, kangwebm, kangMyAss

emojiss = [
    "🌚", "😎", "😃", "😁", "😅", "🤗", "😇", "👀",
    "😐", "🤨", "😒", "😱", "🤣", "👌", "😆", "😍", "🧐", "😑"
]
BOT_USERNAME = "Mr_StarkBot"


@Client.on_message(filters.command(["kang"]))
@error_handler
async def kang(c, m):
    user_id = None
    if m.from_user:
        user_id = str(m.from_user.id)
        print(f"kang {user_id}, {m.from_user.first_name}")
    else:
        await m.reply_text("`Message as a user !`")
        return
    if user_id:
#        await c.send_chat_action(m.chat.id, CHOOSE_STICKER)
        msg = m
        user = m.from_user
        chat_id = m.chat.id
        if os.path.isfile(f"{user_id}.png"):
            try:
                os.remove("{user_id}.png")
            except:
                pass
        if os.path.isfile("{user_id}.tgs"):
            try:
                os.remove("{user_id}.tgs")
            except:
                pass
        if m.reply_to_message:
            if msg.reply_to_message.sticker:
                if msg.reply_to_message.sticker.is_animated == True:
                    file_id = msg.reply_to_message.sticker.file_id
                    await kangani(c, m)
                elif msg.reply_to_message.sticker.is_video == True:
                    file_id = msg.reply_to_message.sticker.file_id
                    await kangwebm(m, c)
                else:
                    await kangMyAss(m, c, chat_id)
            elif msg.reply_to_message.sticker or msg.reply_to_message.photo:
                await kangMyAss(m, c, chat_id)
        else:
            packs = "`Please reply to a sticker or image to kang it!"
            await m.reply_text(packs)


@Client.on_message(filters.command("mypacks"))
@error_handler
async def my_packs(c, m):
    user_id = None
    if m.from_user:
        user_id = str(m.from_user.id)
        user = m.from_user
    else:
        await m.reply_text("Message as a user !")
        return
    packs = f"**{m.from_user.first_name}'s sticker packs:**\n"
    packs1 = ""
    packs2 = ""
    packname = "kang_" + str(user_id) + "_by_"+str(BOT_USERNAME)
    try:
        stickerset = await c.invoke(
            functions.messages.GetStickerSet(
                stickerset=types.InputStickerSetShortName(
                    short_name=packname
                ),
                hash=0
            )
        )
        packnum = 1
    except Exception as e:
        print(f"Error getting sticker set: {e}")
        packnum = 0

    if packnum > 0:
        onlypack = 0
        while onlypack == 0:
            try:
                stickerset = await c.invoke(
                    functions.messages.GetStickerSet(
                        stickerset=types.InputStickerSetShortName(
                            short_name=packname
                        ),
                        hash=0
                    )
                )
                packs += f"[Pack{packnum}](t.me/addstickers/{packname})\n"

            except Exception as e:
                print(f"Error getting sticker set: {e}")
                onlypack = 1

            packnum += 1
            packname = "kang_" + \
                str(packnum - 1) + "_" + str(user_id) + \
                "_by_"+str(BOT_USERNAME)

    packname = "kang_" + str(user.id) + "animated_by_" + str(BOT_USERNAME)
    try:
        stickerset = await c.invoke(
            functions.messages.GetStickerSet(
                stickerset=types.InputStickerSetShortName(
                    short_name=packname
                ),
                hash=0
            )
        )
        packnum = 1
    except Exception as e:
        print(f"Error getting sticker set: {e}")
        packnum = 0

    if packnum > 0:
        onlypack = 0
        packs1 += "**Animatied packs:**\n"
        while onlypack == 0:
            try:
                stickerset = await c.invoke(
                    functions.messages.GetStickerSet(
                        stickerset=types.InputStickerSetShortName(
                            short_name=packname
                        ),
                        hash=0
                    )
                )
                packs1 += f"[Pack{packnum}](t.me/addstickers/{packname})\n"

            except Exception as e:
                print(f"Error getting sticker set: {e}")
                onlypack = 1

            packnum += 1
            packname = "kang_" + \
                str(packnum) + "_" + str(user.id) + \
                "animated_by_"+str(BOT_USERNAME)

    packname = "kang_" + str(user.id) + "video_by_"+str(BOT_USERNAME)
    try:
        stickerset = await c.invoke(
            functions.messages.GetStickerSet(
                stickerset=types.InputStickerSetShortName(
                    short_name=packname
                ),
                hash=0
            )
        )
        packnum = 1
    except Exception as e:
        print(f"Error getting sticker set: {e}")
        packnum = 0

    if packnum > 0:
        onlypack = 0
        packs2 += "**Video sticker pack:**\n"
        while onlypack == 0:
            try:
                stickerset = await c.invoke(
                    functions.messages.GetStickerSet(
                        stickerset=types.InputStickerSetShortName(
                            short_name=packname
                        ),
                        hash=0
                    )
                )
                packs2 += f"[Pack{packnum}](t.me/addstickers/{packname})\n"

            except Exception as e:
                print(f"Error getting sticker set: {e}")
                onlypack = 1

            packnum += 1
            packname = "kang_" + \
                str(packnum) + "_" + str(user.id) + \
                "video_by_"+str(BOT_USERNAME)

    await m.reply_text(f"\n{packs}{packs1}{packs2}")

@Client.on_message(filters.command(["delsticker", "delete_sticker"]))
@error_handler
async def delsticker(c, m):
    user_id = None
    if m.from_user:
        user_id = str(m.from_user.id)
        print(f"del {user_id}, {m.from_user.first_name}")
    else:
        await m.reply_text("Message as a user !")
        return
    if user_id:
        if m.reply_to_message and m.reply_to_message.sticker:
            stickerset = m.reply_to_message.sticker.set_name
        else:
            await m.reply_text(
                "`What Should i delete!`")
            return
        try:
            if str(stickerset)[5:].startswith(str(user_id)):
                await c.send_chat_action(m.chat.id, enums.ChatAction.CHOOSE_STICKER)
            else:
                await m.reply_text("You can only delete stickers from your own packs.")
        except Exception as e:
            await m.reply_text(f"Error deleting sticker: {e}")
