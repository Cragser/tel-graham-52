from dotenv import load_dotenv

from src.application.target_message.create_target_message import create_target_message


def main():
    load_dotenv()
    create_target_message()


main()
