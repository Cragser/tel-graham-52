from src.infrastructure.peewee.database import database as db

def create_table(entity):
    database = db();
    database.create_tables([entity])
