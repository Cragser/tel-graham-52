from src.infrastructure.peewee.create_table import create_table
from src.domain.Channel import Channel


def create_channel_table():
    create_table(Channel)
    
