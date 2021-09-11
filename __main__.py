from dotenv import load_dotenv

from app.controller.channel.get_channels_from_user_controller import get_channels_from_user_controller
from app.controller.telethon_login.validate_telethon_controller import validate_telethon_controller


def main():
    load_dotenv()
    validate_telethon_controller()
    print('hello world')
    # save_channel_from_campaign_controller(1)
    # create_target_message()


main()
