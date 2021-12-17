# Code By @paulwalker_tg

import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.new_chat_members)
async def join(client, message):
    new_member = message.new_chat_members[0]
    msg = await message.reply_video("https://telegra.ph/file/eb5a9eb59358b46320b1a.mp4",
                caption = f"""
**Hey {new_member.first_name},**
**മച്ചാനെ Welcome , മടിക്കേണ്ട കൂട്ടുകാർക്കും ഷെയർ ചെയ്തോ ഗ്രൂപ്പ്‌ പവർ ആകട്ടെ... 💗✌️**
""", parse_mode="md",
     reply_markup = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("🌸 Test Button Nun 🌸", url="https://t.me/tg://settings")
      ],
      [
        InlineKeyboardButton("⚡️ Deploy ⚡️", url="https://telegra.ph/file/a37f19af38c4a0c2f1f74.jpg")
     ]]))

    await asyncio.sleep(50)
    await msg.delete()
