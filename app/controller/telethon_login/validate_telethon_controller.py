from src.infrastructure.telethon.client import validate_telethon


async def validate_telethon_controller():
    await validate_telethon()
