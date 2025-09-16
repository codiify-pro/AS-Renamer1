from pyrogram import filters
from config import Config
from utils.database import get_user_count

def register_stats(app):
    @app.on_message(filters.command("stats") & filters.user(Config.ADMINS))
    async def stats_handler(client, message):
        count = await get_user_count()
        await message.reply_text(f"📊 Total Users in DB: {count}")
