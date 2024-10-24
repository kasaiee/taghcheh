from rest_framework import serializers
from app_book.models import Book
from django.contrib.auth import get_user_model


User = get_user_model()


class AuthorSerizlier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return AuthorSerizlier(obj.author.all(), many=True).data

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'category', 'price']