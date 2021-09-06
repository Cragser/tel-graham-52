from src.domain.Campaign import Campaign


def find_by_name(campaign_name):
    return Campaign.get(Campaign.name == campaign_name)
    
