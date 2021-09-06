from telethon.sync import TelegramClient

PHONE = '+525548798065'

def get_telethon_number():
    return PHONE

def get_telethon_client():
    api_id = 7446084        # YOUR API_ID
    api_hash = '6e7412c6a65abbd5b867820314f3b5a3'        # YOUR API_HASH
    phone = PHONE
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
    return client
