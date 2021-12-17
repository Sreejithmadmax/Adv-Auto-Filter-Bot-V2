# Code By @paulwalker_tg

import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.new_chat_members)
async def join(client, message):
    new_member = message.new_chat_members[0]
    msg = await message.reply_video("https://telegra.ph/file/eb5a9eb59358b46320b1a.mp4",
                caption = f"""
**Hey {new_member.first_name}❤️,**
**Welcome To ★Ⓜ️🌀𝚅𝙸𝙴𝚂_𝙲𝙻𝚄𝙱™★,\n മടിക്കേണ്ട കൂട്ടുകാർക്കും ഷെയർ ചെയ്തോ ഗ്രൂപ്പ്‌ പവർ ആകട്ടെ...\n⭕️താഴെ കാണുന്ന ബട്ടനുകളിൽ ക്ലിക്ക് ചെയ്ത് ജോയിൻ ചെയ്താലേ ഇവിടെ ആവശ്യപ്പെടുന്ന മൂവി ലിങ്ക് വർക്ക്‌ ചെയൂ🤝\n\n📌(𝕄𝕦𝕤𝕥 𝕁𝕠𝕚𝕟 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤)👇**
""", parse_mode="md",
     reply_markup = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("Ⓜ️𝕮𝖍𝖆𝖓𝖓𝖊𝖑 𝐈©", url="https://t.me/filterv32"),
        InlineKeyboardButton("Ⓜ️𝕮𝖍𝖆𝖓𝖓𝖊𝖑 𝐈𝐈©", url="https://t.me/mcmarvels"),
      ],
      [
        InlineKeyboardButton("Ⓜ️𝕮𝖍𝖆𝖓𝖓𝖊𝖑 𝐈𝐈𝐈©", url="https://t.me/MCanimes"),
        InlineKeyboardButton("Ⓜ️𝕮𝖍𝖆𝖓𝖓𝖊𝖑 𝐈𝐕©", url="https://t.me/+IK2aZWUBgjkwMjFl"),
      ],
      [
        InlineKeyboardButton("Ⓜ️𝕮𝖍𝖆𝖓𝖓𝖊𝖑 𝐕©", url="https://t.me/+LB7el58sajNlZDg1"),
        InlineKeyboardButton("Ⓜ️𝕮𝖍𝖆𝖓𝖓𝖊𝖑 𝐕𝐈©", url="https://t.me/mcnewmovies"),
      ],
      [
        InlineKeyboardButton("Ⓜ️𝕮𝖍𝖆𝖓𝖓𝖊𝖑 𝐕𝐈𝐈©", url="https://t.me/+zuXcAWX833c0OTA1"),
        InlineKeyboardButton("Ⓜ️𝕮𝖍𝖆𝖓𝖓𝖊𝖑 𝐕𝐈𝐈𝐈©", url="https://t.me/Mclinkzz"),
      ],
      [
        InlineKeyboardButton("🎭༺ʀʊʟɛֆ༻🎭", url="https://telegra.ph/RULES-OF-11-21")
     ]]))

    await asyncio.sleep(10)
    await msg.delete()
