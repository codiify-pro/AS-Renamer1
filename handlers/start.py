from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_start(app):
    @app.on_message(filters.command("start") & filters.private)
    async def start_handler(client, message):
        await message.reply_text(
            f"👋 Hi {message.from_user.mention},\n\n"
            "I am an **Advanced File Renamer Bot**.\n\n"
            "📌 Send me any file and I will give you option to rename it.",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/codiify")]]
            )
        )
