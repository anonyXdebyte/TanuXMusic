from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from TanuMusic import app
from config import BOT_USERNAME

start_txt = """
❖ ʜᴇʏ , ᴛʜᴇʀᴇ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ  ♥︎\n\n● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ❂𐂷 𐤠ƝⰙƝƳƬƸ 𐒄ꓴⳜƖƇ 𐂷❂, ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ꜰɪɴᴅ ɪᴛ ᴏɴ ɪɴᴛᴇʀɴᴇᴛ ɪᴛꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ❂𐂷 𐤠ƝⰙƝƳƬƸ 𐒄ꓴⳜƖƇ 𐂷❂"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/anonymous_botz")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/pgJ.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
