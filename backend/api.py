from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer

class PostViewSet (viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = PostSerializer