from peewee import CharField, ForeignKeyField
from core.database.models import BaseModel


class ApiUser(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()


class Location(BaseModel):
    name = CharField()


class Device(BaseModel):
    name = CharField()
    type_data = CharField()
    login = CharField()
    password = CharField()
    location_id = ForeignKeyField(Location, backref='devices')
    api_user_id = ForeignKeyField(ApiUser, backref='devices')
