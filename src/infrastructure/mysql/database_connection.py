import os

import mysql.connector


def database_connection():
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
