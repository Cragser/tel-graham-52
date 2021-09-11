import os

from peewee import *


def database():
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = MySQLDatabase(
        'telethon',
        host=host,
        user=user,
        password=password
    )
    return database
