from django.contrib import admin
from .models import BlogModel, LikeModel, CommentModel
admin.site.register([BlogModel, LikeModel, CommentModel])
# Register your models here.
