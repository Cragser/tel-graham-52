# function read a file and return a list of lines
from src.infrastructure.file_manager.get_project_app_path import get_project_app_path


def read_file(file: str) -> list[str]:
    my_file = open(file, "r")
    return my_file.readlines()
