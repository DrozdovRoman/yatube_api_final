from rest_framework import viewsets
from .models import Post, Comment, Follow, Group
from .permissions import IsAuthorOrReadOnlyPermissions
from .serializers import (
    PostSerializer,
    CommentSerializer,
    FollowSerializer,
    GroupSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermissions, )
