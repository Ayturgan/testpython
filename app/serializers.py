from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Tag, Profile
import random

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "username", "bio", "location"]
        read_only_fields = ["user"]

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "profile"]

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "author_username", "post_title", "text", "created_at"]
        read_only_fields = ["author", "created_at"]

    def get_or_create_test_user(self):
        """Создает или возвращает случайного тестового пользователя"""
        test_users_data = [
            {'username': 'alice_blogger', 'first_name': 'Alice', 'last_name': 'Johnson', 'email': 'alice@example.com'},
            {'username': 'bob_writer', 'first_name': 'Bob', 'last_name': 'Smith', 'email': 'bob@example.com'},
            {'username': 'carol_author', 'first_name': 'Carol', 'last_name': 'Brown', 'email': 'carol@example.com'},
            {'username': 'david_commenter', 'first_name': 'David', 'last_name': 'Wilson', 'email': 'david@example.com'},
            {'username': 'eva_reader', 'first_name': 'Eva', 'last_name': 'Davis', 'email': 'eva@example.com'},
        ]
        
        # Создаем тестовых пользователей если их нет
        for user_data in test_users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults=user_data
            )
            if created:
                # Создаем профиль для нового пользователя
                from .models import Profile
                Profile.objects.get_or_create(
                    user=user,
                    defaults={
                        'bio': f'Тестовый пользователь {user.first_name}',
                        'location': 'Test City'
                    }
                )
        
        # Возвращаем случайного пользователя
        test_usernames = [data['username'] for data in test_users_data]
        return User.objects.filter(username__in=test_usernames).order_by('?').first()

    def create(self, validated_data):
        request = self.context.get('request', None)
        
        # Если пользователь аутентифицирован - используем его
        if request and hasattr(request, "user") and request.user.is_authenticated:
            validated_data['author'] = request.user
        else:
            # Иначе назначаем случайного тестового пользователя
            validated_data['author'] = self.get_or_create_test_user()

        return super().create(validated_data)

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id", "title", "content", "author", "author_username",
            "created_at", "updated_at", "tags", "comments"
        ]
        read_only_fields = ["author", "created_at", "updated_at", "comments"]

    def get_or_create_test_user(self):
        """Создает или возвращает случайного тестового пользователя"""
        test_users_data = [
            {'username': 'alice_blogger', 'first_name': 'Alice', 'last_name': 'Johnson', 'email': 'alice@example.com'},
            {'username': 'bob_writer', 'first_name': 'Bob', 'last_name': 'Smith', 'email': 'bob@example.com'},
            {'username': 'carol_author', 'first_name': 'Carol', 'last_name': 'Brown', 'email': 'carol@example.com'},
            {'username': 'david_commenter', 'first_name': 'David', 'last_name': 'Wilson', 'email': 'david@example.com'},
            {'username': 'eva_reader', 'first_name': 'Eva', 'last_name': 'Davis', 'email': 'eva@example.com'},
        ]
        
        # Создаем тестовых пользователей если их нет
        for user_data in test_users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults=user_data
            )
            if created:
                # Создаем профиль для нового пользователя
                from .models import Profile
                Profile.objects.get_or_create(
                    user=user,
                    defaults={
                        'bio': f'Тестовый пользователь {user.first_name}',
                        'location': 'Test City'
                    }
                )
        
        # Возвращаем случайного пользователя
        test_usernames = [data['username'] for data in test_users_data]
        return User.objects.filter(username__in=test_usernames).order_by('?').first()

    def create(self, validated_data):
        request = self.context.get('request', None)
        
        # Если пользователь аутентифицирован - используем его
        if request and hasattr(request, "user") and request.user.is_authenticated:
            validated_data['author'] = request.user
        else:
            # Иначе назначаем случайного тестового пользователя
            validated_data['author'] = self.get_or_create_test_user()
            
        post = super().create(validated_data)
        return post