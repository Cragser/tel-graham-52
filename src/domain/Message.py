from src.infrastructure.peewee.database import database as db
from peewee import *


class Message(Model):
    id = IntegerField(primary_key=True, unique=True, null=False)
    number = CharField(null=False)
    user = CharField(null=False)
    campaign = CharField(null=False)

    class Meta:
        database = db()

    def __str__(self):
        return f'{self.name}'
