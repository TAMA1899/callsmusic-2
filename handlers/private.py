from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""❌❌❌❌SELAMAT DATANG DI ROBOT MUSIC!❌❌❌❌

SAYA AKAN MEMBANTU MEMUTAR MUSIC DI VOICE CHAT GRUB ANDA. 
PERINTAH YANG DAPAT ANDA GUNAKAN :
🎬 /play - __untuk memutar dari audio file atau YouTube link.__
🎬 /pause - __Menghentikan Voice Chat Music.__
🎬 /resume - __Melanjutkan Voice Chat Music.__
🎬 /skip - __untuk melanjutkan Music selanjutnya In Voice Chat.__
🎬 /stop - __menghentikan Voice Chat Music.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group 💬", url="https://t.me/joinchat/jhjQySLPqmBjMGZl"
                    ),
                    InlineKeyboardButton(
                        "Channel 📣", url="https://t.me/pejuangairdrops"
                    )
                ]
            ]
        )
    )
