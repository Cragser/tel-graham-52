from src.infrastructure.telethon.client import get_telethon_client
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random
import re


client = get_telethon_client()
# chat = client.get_entity("https://t.me/LaMejorEstrategiaCriptomonedas")


def main():
    return
    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    # chats.extend(result.chats)

    for chat in chats:
        try:
            print(chat)
            groups.append(chat)
            # if chat.megagroup== True:
        except:
            continue

    print('Choose a group to scrape members from:')
    i = 0
    for g in groups:
        print(str(i) + '- ' + g.title)
        i += 1

    g_index = input("Enter a Number: ")
    target_group = groups[int(g_index)]

    print('\n\nGrupo elegido:\t' + groups[int(g_index)].title)

    print('Fetching Members...')
    all_participants = []
    all_participants = client.get_participants(target_group, aggressive=True)

    print('Saving In file...')
    with open("members-" + re.sub("-+", "-", re.sub("[^a-zA-Z]", "-", str.lower(target_group.title))) + ".csv", "w", encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(['username', 'user id', 'access hash',
                        'name', 'group', 'group id'])
        for user in all_participants:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ""
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ""
            name = (first_name + ' ' + last_name).strip()
            writer.writerow([username, user.id, user.access_hash,
                            name, target_group.title, target_group.id])
    print('Members scraped successfully.')


def get_users_from_chanel(channel_url = None):
    print(channel_url)
    with client:
        client.loop.run_until_complete(main())
