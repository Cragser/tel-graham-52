from src.domain.ChannelCampaign import ChannelCampaign
from src.domain.Campaign import Campaign
from src.infrastructure.peewee.create_table import create_table

def create_campaign_channel_table():
    create_table(ChannelCampaign)
