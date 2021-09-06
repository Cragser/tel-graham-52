from src.infrastructure.telethon.client import get_telethon_client
from telethon.sync import TelegramClient


client = get_telethon_client()

def send_message(username,message):
    client.send_message(username, message)
    # save message
    # send telegramn message