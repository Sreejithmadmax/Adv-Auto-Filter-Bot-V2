# Â© @paulwalker_tg
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from bot.plugins.Paulwalker_tg.user_db import get_users
from bot.plugins.Paulwalker_tg.user_db import del_from_users
from pyrogram.errors import (FloodWait, PeerIdInvalid, UserIsBlocked, InputUserDeactivated)
    
ADMINS = [1921448473,1442587694]

@Client.on_message(filters.private & filters.command('broadcast'), group=2)
async def broadcast(client, message):

    if not message.from_user.id in ADMINS: return await message.reply_sticker("CAACAgUAAxkBAAEBLDphfSzNDHd5BpbV6dX-wbfTYhOGngAC_wIAAhx6cFWp_hhQj9wZ_R4E")

    if not message.reply_to_message: return await message.reply("🧠 Use Brain If You Don't Have Take Mine , Reply To Something To Broadcast It...")
        
    user_ids = await get_users()
    m = await message.reply('__Broadcasting message, Please wait.......__')    
    
    success = 0
    deleted = 0
    blocked = 0
    peerid = 0
    
    for user_id in user_ids:
        try:
            await message.reply_to_message.copy(user_id)
            success += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await message.copy(user_id)
            success += 1

        except UserIsBlocked:
            blocked += 1
            await del_from_userbase(user_id)

        except PeerIdInvalid:
            peerid += 1

        except InputUserDeactivated:
            deleted += 1
            await del_from_userbase(user_id)
            
    await m.edit(f"""
**🤝 Broadcast Completed.**
    
**Total users:** {str(len(user_ids))}
**Blocked users:** {str(blocked)}
**Deleted accounts:** {str(deleted)}
**Send Failed:** {str(peerid)}
""")
