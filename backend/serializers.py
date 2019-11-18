from rest_framework import serializers

from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =('author', 'title', 'body'),
        model = Comment
        fields = ('author', 'body', 'post')