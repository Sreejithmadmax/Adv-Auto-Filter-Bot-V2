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
            member = await bot.get_chat_member(-1001372299086, update.chat.id)
            if member.status == "kicked":
                await bot.send_message(
                       chat_id=update.chat.id,
                       text="Sorry mate!  You're  B A N N E D 🥱",
                       reply_to_message_id=update.message_id
                       )
                return
        
        except UserNotParticipant:
            me = await bot.get_me()
            await bot.send_message(
                    chat_id=update.chat.id,
                    text="You Need To Join Our Channel and Press Refresh Button to get the file.",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Join Channel",url="https://t.me/joinchat/+IK2aZWUBgjkwMjFl")],
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
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/CrazyBotsz"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/Rihu_mone"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/Rihu_mone"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('Developers', url='https://t.me/Rihu_mone'),
        InlineKeyboardButton('Source Code 🧾', url ='https://t.me/BWF_ofc/2')
    ],[
        InlineKeyboardButton('Support 🛠', url='https://t.me/joinchat/c-r6fPf_UqwxMmE9')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
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
