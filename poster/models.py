from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()