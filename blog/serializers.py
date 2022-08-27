from rest_framework import serializers
from .models import BlogModel, CommentModel, LikeModel


class BlogSerializer(serializers.ModelSerializer):
    writterName = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'content',
                  'blogType', 'createdAt', 'writterName']


class LikeSerializer(serializers.ModelSerializer):
    blog = serializers.ReadOnlyField(source="blog.title")
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = LikeModel
        fields = ['blog', 'user', 'is_liked']

    def create(self, validated_data):
        query = LikeModel.objects.filter(blog=validated_data['blog'])
        if not query:
            return LikeModel.objects.create(**validated_data)
        else:
            query = query[0]

        if query.is_liked == False:
            query.is_liked = True
            query.save()
            return query
        elif query.is_liked == True:
            query.is_liked = False
            query.save()
            return query


class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.ReadOnlyField(source="blog.id")
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = CommentModel
        fields = ['id', 'blog', 'user', 'comment', 'createdAt']
