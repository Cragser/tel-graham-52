import datetime
from src.infrastructure.peewee.database import database as db
from peewee import *


class TargetMessage(Model):
    id = AutoField(primary_key=True)
    number = IntegerField()
    username = CharField()
    userid = CharField()
    name = CharField()
    message = TextField()
    campaign = IntegerField(default=1)
    sended_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db()

    def __str__(self):
        return f'{self.number}'
