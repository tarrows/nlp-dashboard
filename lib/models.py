from tortoise.models import Model
from tortoise import fields


class Story(Model):
    id = fields.IntField()
    title = fields.TextField()
    url = fields.TextField()
    score = fields.IntField()
    by = fields.TextField()
    time = fields.IntField()

    def __str__(self):
        return f'{self.id} {self.title}'
