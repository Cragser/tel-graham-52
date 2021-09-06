from src.domain.Campaign import Campaign
from src.infrastructure.peewee.create_table import create_table

def create_campaign_table():
    create_table(Campaign)
