import os

from telethon.sync import TelegramClient

PHONE = os.getenv('PHONE')


def get_telethon_number():
    return PHONE


def _get_telegram_client():
    api_id = os.getenv('TELEGRAM_API_ID')  # YOUR API_ID
    api_hash = os.getenv('TELEGRAM_API_HASH')  # YOUR API_HASH
    phone = PHONE
    return TelegramClient(phone, api_id, api_hash)


def get_telethon_client():
    client = _get_telegram_client()
    client.connect()
    return client


async def validate_telethon():
    with _get_telegram_client() as client:
        client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))


def get_client_with_token():
    bot_token = os.getenv('TELEGRAM_TOKEN')
    return _get_telegram_client().start(bot_token=bot_token)
