import os

from src.infrastructure.file_manager.get_project_app_path import get_project_app_path
from src.infrastructure.file_manager.read_file import read_file


def get_messages_path():
    language = os.getenv('LANGUAGE')
    server_path = get_project_app_path();
    return f'{server_path}/data/files/messages_{language}.txt'


def get_messages():
    return read_file(get_messages_path())
