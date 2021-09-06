from src.infrastructure.peewee.create_ignore_duplicate import create_ignore_duplicate
from src.domain.ChannelCampaign import ChannelCampaign
from src.domain.Channel import Channel


def save_channel_from_campaign(campaign_id, channels):

    for channel_url in channels:
        create_ignore_duplicate(Channel,'url', channel_url)
        
        # channel = Channel(url = channel_url)

        # channel.save()
        # channel_id = channel.get_id()
        # channel_campaign = ChannelCampaign(
        #     channel_id = channel_id,
        #     campaign_id = campaign_id
        # )
        # channel_campaign.save()