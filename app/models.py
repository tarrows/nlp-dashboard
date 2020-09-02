from tortoise.models import Model
from tortoise import fields


class Story(Model):
    id = fields.IntField()
    title = fields.TextField()

    def __str__(self):
        return f'{self.id} {self.title}'
