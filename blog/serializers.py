from rest_framework import serializers
from .models import BlogModel


class BlogSerializer(serializers.ModelSerializer):
    writterName = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'content',
                  'blogtype', 'createdAt', 'writterName']
