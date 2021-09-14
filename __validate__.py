from dotenv import load_dotenv

from src.infrastructure.telethon.client import _get_telegram_client

load_dotenv()
client = _get_telegram_client();

async def main():
    await (client.send_message('me', 'Hello, myself!'))


with client:
    client.loop.run_until_complete(main())
