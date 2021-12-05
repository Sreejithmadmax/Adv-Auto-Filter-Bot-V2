#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption =f"<code><b> {file_name}</b> </code>\n<b>❤️Join [★Ⓜ️🌀𝚅𝙸𝙴𝚂_𝙲𝙻𝚄𝙱_𝟸⭕️𝟷𝟿™★] For New Movies.</b>\n❤️<u> 𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚄𝚜 𝙱𝚢 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙾𝚞𝚛 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙶𝚛𝚘𝚞𝚙 𝙻𝚒𝚗𝚔 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚜</u> \n\n❁𝕁𝕠𝕚𝕟 𝕆𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤❁  \n⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱  \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @mcmarvels➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑 : @mcallmovies➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @mcnewmovies➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @MCmoviesall➻ \n",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝑺𝑯𝑨𝑹𝑬', url="https://t.me/share/url?url=https://t.me/share/url?url=https://t.me/Movies_Club_2019")
                ],
                [
                    InlineKeyboardButton('♻️𝐌𝐎𝐕𝐈𝐄𝐑𝐄𝐐', url="https://t.me/Movies_Club_2019"),
                    InlineKeyboardButton('𝐒𝐄𝐑𝐈𝐄𝐒🔰', url="https://t.me/MoviesClubSeriesonly")
                ],
                [
                    InlineKeyboardButton('〽️©◥ʟɨռӄʐʐ◤', url="https://t.me/Mclinkzz"),
                    InlineKeyboardButton('𝐔𝐏𝐃𝐀𝐓𝐄📽️', url="https://t.me/ottmovies_updates")
                ]
            ]
        )
    )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('Dev ✨️', url="https://t.me/Dorakutty"),
        InlineKeyboardButton('Close 💔', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_sticker(
        chat_id=update.chat.id,
        sticker= "CAACAgIAAxkBAAEBSqthkjttlt0G5Byj7Eq1qRucBVR0wQAC1AwAAnqLoEieLyIklDO8mx4E",
        reply_markup=reply_markup,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Dev ✨️', url="https://t.me/Dorakutty"),
        InlineKeyboardButton('Close 💔', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_sticker(
        chat_id=update.chat.id,
        sticker= "CAACAgIAAxkBAAEBSp1hkjljLaP-qN6BNBV22JpfzhPV-wACzxEAAud1mUikiFSKzlb3ZB4E",
        reply_markup=reply_markup,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Dev ✨️', url="https://t.me/Dorakutty"),
        InlineKeyboardButton('Close 💔', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_sticker(
        chat_id=update.chat.id,
        sticker= "CAACAgIAAxkBAAEBSqNhkjmJai0tXFRHtq8fTXyYWcSJygACZg8AAlGwsEiUHH3OCPuZqR4E",
        reply_markup=reply_markup,
        reply_to_message_id=update.message_id
    )
