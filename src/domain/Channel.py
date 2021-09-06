from src.infrastructure.peewee.database import database as db
from peewee import *


class Channel(Model):
    id = AutoField(primary_key=True)
    url = CharField(unique=True)
    status = CharField(null=False, default='A')

    class Meta:
        database = db()

    def __str__(self):
        return f'{self.url}'
