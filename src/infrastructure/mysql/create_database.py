from src.infrastructure.mysql.database_connection import database_connection


def create_database():
    mydb = database_connection()
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE telethon")

