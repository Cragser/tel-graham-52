from src.infrastructure.mysql.database_connection import database_connection


def show_databases():
    db = database_connection()
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    for row in cursor:
        print(row)
    cursor.close()

