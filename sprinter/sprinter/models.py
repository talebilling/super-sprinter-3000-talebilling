from sprinter.connectdatabase import DatabaseConnection
from peewee import *


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = DatabaseConnection.db


class Story(BaseModel):
    title = CharField()
    story = CharField()
    criteria = CharField()
    business = IntegerField()
    estimation = FloatField()
    status = CharField()
