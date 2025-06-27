from telethon.sync import TelegramClient
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

with TelegramClient("session", API_ID, API_HASH) as client:
    print("✅ Logged in and session saved.")
