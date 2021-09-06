from app.infrastructure.telethon import client

def create_from_group(group):
     client.get_participants(group, aggressive=True)