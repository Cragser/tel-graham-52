import csv
import os

from src.application.channel.read_channel_from_csv import read_from_from_csv_iterate
from src.application.message.send_message import send_message
from src.infrastructure.file_manager.get_messages import get_messages
from src.infrastructure.telethon.client import get_telethon_number
import time
from src.domain.TargetMessage import TargetMessage
import sys
import random

NUMBER = get_telethon_number()
messages = get_messages()


def create_message(name) -> str:
    message = random.choice(messages)
    message.replace('{name}', name)
    return message


def user_has_message(userid):
    query = TargetMessage.select().where(TargetMessage.userid == userid)
    return query.exists()


def send_message_and_save(row):
    username = row[0]
    userid = row[1]
    name = row[3]
    message = create_message(name)

    if user_has_message(userid):
        print('Target Message already exists')
    else:
        print('Sending message')
        target_message = TargetMessage(
            number=NUMBER,
            username=(username if username != '' else 'no_username'),
            userid=userid,
            name=name,
            message=message,
        )
        target_message.save()

        if username != '':
            send_message(username, message)
            time_to_wait = random.randint(60 * 5, 60 * 5 + 10)
            print(f'Sending message to {username}, next message in {time_to_wait} seconds')
            time.sleep(time_to_wait)


def create_target_message():
    read_from_from_csv_iterate(send_message_and_save)
