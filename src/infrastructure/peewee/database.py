import os

from dotenv import load_dotenv
from peewee import *

load_dotenv()


def database():
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    print(host, user, password)

    return MySQLDatabase(
        'telethon',
        host=host,
        user=user,
        password=password
    )
