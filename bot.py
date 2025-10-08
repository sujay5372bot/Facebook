from pyrogram import Client, filters
from config import *
from fb_uploader import upload_to_facebook
from premium_manager import is_premium, activate_key

app = Client("FBUploaderBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video)
async def handle_video(client, message):
    user_id = message.from_user.id
    video = await message.download()
    caption = message.caption or "Uploaded from Telegram Bot"

    await message.reply_text("📤 Uploading video to Facebook...")
    result = upload_to_facebook(video, "Telegram Upload", caption, FB_PAGE_ID, FB_ACCESS_TOKEN)

    if "id" in result:
        await message.reply_text(f"✅ Uploaded successfully!\nhttps://www.facebook.com/{result['id']}")
    else:
        await message.reply_text(f"❌ Upload failed:\n{result}")

app.run()
