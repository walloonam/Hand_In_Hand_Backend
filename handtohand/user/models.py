from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10,null=False, default='')
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=10,null=False, default='')
    date_of_birth = models.DateTimeField(max_length=20)
    address = models.CharField(max_length=1000)
    point = models.IntegerField()
    adopt_count = models.IntegerField(default=0)
    area = models.ForeignKey('post.Area', on_delete=models.CASCADE, null=True)


class Attendance(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)