from dotenv import load_dotenv

from src.application.target_message.create_target_message import create_target_message

load_dotenv()


def main():
    create_target_message()


main()
