import string
import random

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


class EmailVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def generate_verification_token(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_verification_token()
        super().save(*args, **kwargs)