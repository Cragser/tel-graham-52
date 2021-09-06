from app.controller.telegram_controller import telegram_controller
from src.application.target_message.create_target_message import create_target_message
from src.application.target_message.create_target_message_table import create_target_message_table
from src.application.campaign.create_campaign_table import create_campaign_table
from src.application.campaign.create_campaign import create_campaign
from src.application.channel.create_channel_table import create_channel_table
from src.application.campaign_channel.create_campaign_channel_table import create_campaign_channel_table
from app.controller.channel.save_channel_from_campaign_controller import save_channel_from_campaign_controller
# from app.controller.telegram import telegram


def main():
    # telegram_controller()
    create_campaign_table()
    create_channel_table()
    create_campaign_channel_table()
    create_target_message_table()

    # save_channel_from_campaign_controller(1)
    create_target_message()


main()
