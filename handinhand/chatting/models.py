from django.db import models

class Room(models.Model):
    image = models.ImageField(upload_to='profile/', null=True)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)

class Content(models.Model):
    content = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chatting/', null=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    room = models.ForeignKey('chatting.Room', on_delete=models.CASCADE, null=True)

