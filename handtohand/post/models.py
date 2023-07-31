from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    point = models.IntegerField(default = 0) # 처음 시작할 때 가지는 포인트로 해야하나
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    area = models.ForeignKey('post.Area', on_delete=models.CASCADE, null=True)



class Area(models.Model):
    name = models.CharField(max_length=10)

