from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser
from .choices import BLOG_TYPES


class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    blogType = models.CharField(max_length=5, choices=BLOG_TYPES)
    createdAt = models.DateTimeField(auto_now=True)
    writter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LikeModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.is_liked}"


class CommentModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.comment}"
