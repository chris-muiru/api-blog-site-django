from django.db import models
from django.contrib.auth.models import User

from writter.models import WritterModel


class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    BLOG_TYPES = (('prog', 'programming'), ('net', 'networking'),
                  ('data', 'data-science'))
    blogtype = models.CharField(max_length=5, choices=BLOG_TYPES)
    createdAt = models.DateTimeField(auto_now=True)
    writter = models.ForeignKey(WritterModel, on_delete=models.CASCADE)


class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=True)


class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=True)
