from mongoengine import connect, Document, StringField, IntField, ReferenceField, ListField, NULLIFY
from decouple import config


connect(
    db=config('DB_NAME'),
    username=config('DB_USER'),
    password=config('DB_PASSWORD'),
    host=config('DB_HOST'),
    port=config('DB_PORT', cast=int)
)


class Theme(Document):
    name = StringField()
    videos = ListField(ReferenceField("Video"))

    @property
    def rating(self):
        up = 0
        down = 0
        for video in self.videos:
            up += video.thumbs_up
            down += video.thumbs_down
        return up - (down/2)


class Video(Document):
    name = StringField()
    thumbs_up = IntField(default=0)
    thumbs_down = IntField(default=0)
    theme = ReferenceField(Theme, reverse_delete_rule=NULLIFY)
