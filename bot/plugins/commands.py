#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        try:
            member = await bot.get_chat_member(-1001569614628, update.chat.id)
            if member.status == "kicked":
                await bot.send_message(
                       chat_id=update.chat.id,
                       text="Sorry mate!🤣  You're  B A N N E D 🥱 Contact Admin👉 @Myfreak123",
                       reply_to_message_id=update.message_id
                       )
                return
        
        except UserNotParticipant:
            me = await bot.get_me()
            await bot.send_message(
                    chat_id=update.chat.id,
                    text="<b><u>🔰You Need To Join Our Channel and Press Refresh Button to get the file</b></u>.\n<b><u>🔰ചാനലിൽ ജോയിൻ ചെയ്ത് Refresh കൊടുത്ത് start കൊടുക്കുക💗</b></u>",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Join Channel",url="https://t.me/+IK2aZWUBgjkwMjFl")],
                                                       [InlineKeyboardButton(text="Refresh", url=f"https://t.me/{me.username}?start={file_uid}")]]),
                    reply_to_message_id=update.message_id
                    )
            return
        
        except Exception:
            print('Unable to Verify')
            await bot.send_message(
                     chat_id=update.chat.id,
                     text="```Something Went Wrong```",
                     parse_mode='markdown',
                     reply_to_message_id=update.message_id
                     )
            return
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption =f"<b>❤️ 𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴<code> {file_name}</code></b>\n<b>❤️ 𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚄𝚜 𝙱𝚢 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙾𝚞𝚛 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙶𝚛𝚘𝚞𝚙 𝙻𝚒𝚗𝚔 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚜</b>\n❁𝕁𝕠𝕚𝕟 𝕆𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤❁  \n⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱\n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @moviesupdats1➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑 : @movies_Club_2018➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @mcnewmovies➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @filterv32➻",
                parse_mode="html",         
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝚂𝙷𝙰𝚁𝙴', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/Movies_Club_2019")
                ],
                [
                    InlineKeyboardButton('𝙼𝙾𝚅𝙸𝙴 𝚁𝙴𝚀', url="https://t.me/Movies_Club_2019"),
                    InlineKeyboardButton('𝚂𝙴𝚁𝙸𝙴𝚂', url="https://t.me/+LB7el58sajNlZDg1")
                ],
                [
                    InlineKeyboardButton('𝙼𝙲 𝙻𝙸𝙽𝙺𝚉', url="https://t.me/Mclinkzz"),
                    InlineKeyboardButton('𝙰𝙽𝙸𝙼𝙴', url="https://t.me/MCanimes")
                ]
            ]
        )
    )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption =f"<b>❤️ 𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴<code> {file_name}</code></b>\n<b>❤️ 𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚄𝚜 𝙱𝚢 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙾𝚞𝚛 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙶𝚛𝚘𝚞𝚙 𝙻𝚒𝚗𝚔 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚜</b>\n❁𝕁𝕠𝕚𝕟 𝕆𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤❁  \n⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱\n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @moviesupdats1➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑 : @movies_Club_2018➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @mcnewmovies➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @filterv32➻",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝚂𝙷𝙰𝚁𝙴', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/Movies_Club_2019")
                ],
                [
                    InlineKeyboardButton('𝙼𝙾𝚅𝙸𝙴 𝚁𝙴𝚀', url="https://t.me/Movies_Club_2019"),
                    InlineKeyboardButton('𝚂𝙴𝚁𝙸𝙴𝚂', url="https://t.me/+LB7el58sajNlZDg1")
                ],
                [
                    InlineKeyboardButton('𝙼𝙲 𝙻𝙸𝙽𝙺𝚉', url="https://t.me/Mclinkzz"),
                    InlineKeyboardButton('𝙰𝙽𝙸𝙼𝙴', url="https://t.me/MCanimes")
                ]
            ]
        )
    )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption =f"<b>❤️ 𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴<code> {file_name}</code></b>\n<b>❤️ 𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚄𝚜 𝙱𝚢 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙾𝚞𝚛 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙶𝚛𝚘𝚞𝚙 𝙻𝚒𝚗𝚔 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚜</b>\n❁𝕁𝕠𝕚𝕟 𝕆𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤❁  \n⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱\n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @moviesupdats1➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑 : @movies_Club_2018➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @mcnewmovies➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @filterv32➻",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝚂𝙷𝙰𝚁𝙴', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/Movies_Club_2019")
                ],
                [
                    InlineKeyboardButton('𝙼𝙾𝚅𝙸𝙴 𝚁𝙴𝚀', url="https://t.me/Movies_Club_2019"),
                    InlineKeyboardButton('𝚂𝙴𝚁𝙸𝙴𝚂', url="https://t.me/+LB7el58sajNlZDg1")
                ],
                [
                    InlineKeyboardButton('𝙼𝙲 𝙻𝙸𝙽𝙺𝚉', url="https://t.me/Mclinkzz"),
                    InlineKeyboardButton('𝙰𝙽𝙸𝙼𝙴', url="https://t.me/MCanimes")
                ]
            ]
        )
    )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('🤴 𝙳𝙴𝚅 🤴', url="https://t.me/BlinderTG"),
        InlineKeyboardButton('🚫 𝙲𝚕𝚘𝚜𝚎 🚫', callback_data='close')
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
        InlineKeyboardButton('🤴 𝙳𝙴𝚅 🤴', url="https://t.me/BlinderTG"),
        InlineKeyboardButton('🚫 𝙲𝚕𝚘𝚜𝚎 🚫', callback_data='close')
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
        InlineKeyboardButton('🤴 𝙳𝙴𝚅 🤴', url="https://t.me/BlinderTG"),
        InlineKeyboardButton('🚫 𝙲𝚕𝚘𝚜𝚎 🚫', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_sticker(
        chat_id=update.chat.id,
        sticker= "CAACAgIAAxkBAAEBSqNhkjmJai0tXFRHtq8fTXyYWcSJygACZg8AAlGwsEiUHH3OCPuZqR4E",
        reply_markup=reply_markup,
        reply_to_message_id=update.message_id
    )
