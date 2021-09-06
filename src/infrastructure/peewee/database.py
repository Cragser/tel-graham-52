from peewee import *


def database():
    database = MySQLDatabase(
        'telethon',
        host="ls-05e88db820c0415c07abb89eec7d3f57e39a3e64.cu5yrqifxqtg.us-east-2.rds.amazonaws.com",
        user='dbmasteruser',
        password='[jbMhN029vJ6:bf2=M+{f&;89p7HaU`Z'
    )
    return database
