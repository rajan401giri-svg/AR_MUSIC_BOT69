from pyrogram import Client, filters
from config import *

app = Client(
    "VoiceBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        "✅ Bot Online Successfully!"
    )

@app.on_message(filters.command("ping"))
async def ping(_, message):
    await message.reply_text("🏓 Pong")

print("Bot Started")

app.run()
