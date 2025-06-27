import os
import asyncio
from telethon import TelegramClient
from telethon.tl.types import InputPeerChannel
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = "session"
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # Example: -1001234567890

DOWNLOAD_DIR = "downloads"

async def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start()

    entity = await client.get_entity(CHANNEL_ID)

    for filename in os.listdir(DOWNLOAD_DIR):
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(('.mp4', '.mkv', '.mov')):
            print(f"Uploading: {filename}")
            try:
                await client.send_file(
                    entity,
                    filepath,
                    caption=filename,
                    video_note=False
                )
                print(f"✅ Uploaded: {filename}")
            except Exception as e:
                print(f"❌ Error uploading {filename}: {e}")

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
