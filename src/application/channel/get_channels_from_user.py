from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

from src.infrastructure.telethon.client import get_telethon_client


def get_channels_from_user():
    chats = []
    last_date = None
    chunk_size = 200
    groups = []
    client = get_telethon_client()
    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            print(chat)
            if chat.megagroup:
                groups.append(chat)
        except:
            continue

    print('Choose a group to scrape members from:')
    i = 0
    for g in groups:
        print(str(i) + '- ' + g.title)
        i += 1
