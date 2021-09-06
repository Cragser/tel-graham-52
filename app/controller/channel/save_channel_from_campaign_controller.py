from src.application.channel.save_channel_from_campaign import save_channel_from_campaign


channels = [
    'https://t.me/linkspromoter',
    'https://t.me/smartpeoplechat'
]

def save_channel_from_campaign_controller(campaign):
    # get channel from this campaign
    
    save_channel_from_campaign(1, channels)
        
