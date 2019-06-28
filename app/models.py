from mongoengine import connect, Document, StringField, IntField
from decouple import config


connect(config('DB_NAME'), host=config('DB_HOST'), port=config('DB_PORT'))


class Video(Document):
    name = StringField()
    thumbs_up = IntField()
    thumbs_down = IntField()


class Theme(Document):
    name = StringField()
