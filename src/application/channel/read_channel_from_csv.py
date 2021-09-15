# function that read channel from csv file
import csv
from os import system
import os

from dotenv import load_dotenv

from src.infrastructure.file_manager.get_project_app_path import get_project_app_path

load_dotenv()

def get_csv_path():
    filename = os.getenv("CSV_FILE")
    server_path = get_project_app_path()
    return f'{server_path}/data/{filename}.csv'


def read_from_from_csv_iterate(callback):
    path = get_csv_path()
    with open(path, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            callback(row)
