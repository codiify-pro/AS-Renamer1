import os, asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

def register_rename(app):
    @app.on_message(filters.document | filters.video)
    async def file_handler(client, message):
        file = message.document or message.video
        fname = file.file_name

        keyboard = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("✏️ Rename", callback_data=f"rename:{file.file_id}"),
                InlineKeyboardButton("❌ Cancel", callback_data="cancel")
            ]]
        )

        await message.reply_text(
            f"📂 File received: `{fname}`\n\n👉 Choose an action:",
            reply_markup=keyboard
        )

    @app.on_callback_query(filters.regex(r"^rename:(.*)"))
    async def rename_callback(client, callback_query):
        file_id = callback_query.data.split(":")[1]
        await callback_query.message.reply_text("✏️ Send me new filename (with extension).")

        response = await client.listen(callback_query.from_user.id, filters=filters.text)
        new_name = response.text.strip()

        try:
            file = await client.download_media(file_id)
            new_file_path = f"{new_name}"
            os.rename(file, new_file_path)

            await client.send_document(
                callback_query.from_user.id,
                new_file_path,
                caption=f"✅ Renamed to `{new_name}`"
            )
            os.remove(new_file_path)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            await callback_query.message.reply_text(f"❌ Error: {e}")
