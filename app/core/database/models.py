from playhouse.migrate import Model
from .manager import db


class BaseModel(Model):
    class Meta:
        database = db.database
