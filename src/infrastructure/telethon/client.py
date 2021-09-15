import os

from dotenv import load_dotenv
from telethon.sync import TelegramClient
load_dotenv()
PHONE = os.getenv('PHONE')
API_ID = os.getenv('TELEGRAM_API_ID')  # YOUR API_ID
API_HASH = os.getenv('TELEGRAM_API_HASH')  # YOUR API_HASH

if API_ID == '':
    raise Exception("API ID IS EMPTY")

if API_HASH == '':
    raise Exception("API HASH IS EMPTY")

def get_telethon_number():
    return PHONE


def _get_telegram_client():
    return TelegramClient(PHONE, API_ID, API_HASH)


def get_telethon_client():
    client = _get_telegram_client()
    client.connect()
    client.start()
    return client


async def validate_telethon():
    with _get_telegram_client() as client:
        client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))


