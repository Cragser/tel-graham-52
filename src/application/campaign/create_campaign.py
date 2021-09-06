from peewee import AutoField
from src.domain.Campaign import Campaign
from datetime import date


def create_campaign(name):
    campaign = Campaign(
        name=name,
        startDate=date(year=2021, month=8, day=30),
    )
    campaign.save(force_insert=True)
