from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'comments', views.CommentViewSet, basename='comment')
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'profiles', views.ProfileViewSet, basename='profile')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
]