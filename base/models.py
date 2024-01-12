from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, SET_NULL, ManyToManyField
from django.contrib.auth.models import User

# Create your models here.
class Topic(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(Model):
    host = ForeignKey(User, on_delete=SET_NULL, null=True)
    topic = ForeignKey(Topic, on_delete=SET_NULL, null=True)
    name=CharField(max_length=100)
    description=TextField()
    participants=ManyToManyField(User, related_name="participants", blank=True)
    updated=DateTimeField(auto_now=True)
    created=DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-updated", "-created"]

    def __str__(self):
        return self.name

class Message(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    room = ForeignKey(Room, on_delete=CASCADE)
    body = TextField()
    updated=DateTimeField(auto_now=True)
    created=DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

