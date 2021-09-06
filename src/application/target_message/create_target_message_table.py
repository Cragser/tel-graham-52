from src.infrastructure.peewee.create_table import create_table
from src.domain.TargetMessage import TargetMessage


def create_target_message_table():
    create_table(TargetMessage)
    
