import csv
import os

from src.infrastructure.telethon.client import get_telethon_number
import time
from src.application.message.send_message import send_message
from src.domain.TargetMessage import TargetMessage
import sys
import threading
from random import randint

NUMBER = get_telethon_number()


def create_target_message():
    path = sys.path[0] + \
           f'/data/{os.getenv("CSV_FILE")}.csv'
    with open(path, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            username = row[0]
            userid = row[1]
            name = row[3]

            message = f'Hi {name} We are looking for people like you, with leadership ang willing to be part of the first Smart Contract with which you can generate permanent residual money, in addition, it´s a transparent and secure decentralized system where you can have all the right tools to grow your money Are you willing to accept this growth opportunity?'
            # message2 = 'Learn more about us on: https://thesmartway.io/c/b15840'
            message2 = ''

            query = TargetMessage.select().where(TargetMessage.userid == userid)
            if query.exists():
                print('Target Message already exists')
            else:
                target_message = TargetMessage(
                    number=NUMBER,
                    username=(username if username != '' else 'no_username'),
                    userid=userid,
                    name=name,
                    message=message,
                )
                target_message.save()
                if (username != ''):
                    send_message(username, message + ' ' + message2)
                    time_to_wait = randint(30, 55)
                    print(
                        f'Sending message to {username}, next message in {time_to_wait} seconds')
                    time.sleep(time_to_wait)
            # create_message
            # if not message sended
            # send_message
            # print(row)
