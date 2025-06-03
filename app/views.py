from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Post, Comment, Tag, Profile
from .serializers import (
    PostSerializer, CommentSerializer, TagSerializer, ProfileSerializer, UserSerializer
)

class PostViewSet(viewsets.ModelViewSet):
    """API endpoint, который позволяет просматривать и редактировать посты."""
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

class CommentViewSet(viewsets.ModelViewSet):
    """API endpoint для комментариев."""
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

class TagViewSet(viewsets.ModelViewSet):
    """API endpoint для тегов."""
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProfileViewSet(viewsets.ModelViewSet):
    """API endpoint для профилей пользователей."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint для просмотра пользователей."""
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


def interface(request):
    return render(request, 'app_interface.html')
