from src.infrastructure.peewee.database import database as db
from peewee import *


class Campaign(Model):
    id = AutoField(primary_key=True)
    name = CharField(unique=True)
    startDate = DateTimeField()
    endDate = DateTimeField(null=True)
    totalMessages = IntegerField(default=0)
    status = IntegerField(default='A')

    class Meta:
        database = db()
