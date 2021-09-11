from dotenv import load_dotenv
from app.controller.telethon_login.validate_telethon_controller import validate_telethon_controller
from src.infrastructure.telethon.client import get_client_with_token


def main():
    load_dotenv()
    validate_telethon_controller()
    print('hello world')

    # telegram_controller()

    # create_campaign_table()
    # create_channel_table()
    # create_campaign_channel_table()
    # create_target_message_table()

    # save_channel_from_campaign_controller(1)
    # create_target_message()


main()
