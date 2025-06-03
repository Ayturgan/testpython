from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Tag, Profile

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

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "author_username", "text", "created_at"]
        read_only_fields = ["author", "created_at"]

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, "user") and request.user.is_authenticated:
            validated_data['author'] = request.user
        elif 'author' not in validated_data:
             raise serializers.ValidationError("Author could not be determined from request context.")

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

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, "user") and request.user.is_authenticated:
            validated_data['author'] = request.user
        elif 'author' not in validated_data:
             raise serializers.ValidationError("Author could not be determined from request context.")
        post = super().create(validated_data)
        return post