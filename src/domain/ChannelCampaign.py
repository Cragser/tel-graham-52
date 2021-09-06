from src.infrastructure.peewee.database import database as db
from peewee import Model, CharField, IntegerField, ForeignKeyField, PrimaryKeyField, TextField
from src.domain.Channel import Channel
from src.domain.Campaign import Campaign


class ChannelCampaign(Model):
    id = IntegerField(primary_key=True, unique=True, null=False)
    channelId = ForeignKeyField(Channel, null=False)
    campaignId = ForeignKeyField(Campaign, null=False)

    class Meta:
        database = db()
