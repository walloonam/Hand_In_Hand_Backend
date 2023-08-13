from django.db import models

class Room(models.Model):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True,related_name="owner")
    customer = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, related_name='customer')

class Content(models.Model):
    content = models.CharField(max_length=50)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    room = models.ForeignKey('chatting.Room', on_delete=models.CASCADE, null=True)

