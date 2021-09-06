from peewee import *

database = MySQLDatabase(
    'telethon',
    host="ls-05e88db820c0415c07abb89eec7d3f57e39a3e64.cu5yrqifxqtg.us-east-2.rds.amazonaws.com",
    user='dbmasteruser',
    password='[jbMhN029vJ6:bf2=M+{f&;89p7HaU`Z'
)


class Campaign(Model):
    id = AutoField(primary_key=True, unique=True, null=False)
    name = CharField(unique=True)
    startDate = DateTimeField()
    endDate = DateTimeField(null=True)
    totalMessages = IntegerField(default=0)
    status = IntegerField(default='A')

    class Meta:
        database = database

    def __str__(self):
        return f'{self.name}'


def create_all_campaign_table():
    database.create_tables([Campaign])
