from tokenize import Comment
from rest_framework import serializers
from .models import BlogModel, CommentModel, LikeModel


class BlogSerializer(serializers.ModelSerializer):
    writterName = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'content',
                  'blogtype', 'createdAt', 'writterName']


class LikeSerializer(serializers.ModelSerializer):
    blog = serializers.ReadOnlyField(source="blog.title")
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = LikeModel
        fields = ['blog', 'user', 'is_liked']

    def create(self, validated_data):
        print(validated_data)
        query = LikeModel.objects.filter(blog=validated_data['blog'])
        if query:
            query[0].is_liked = True
            query[0].save()
            return query[0]
        else:
            return LikeModel.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.ReadOnlyField(source="blog.id")
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = CommentModel
        fields = ['id', 'blog', 'user', 'comment', 'createdAt']
