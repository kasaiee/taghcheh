from django.shortcuts import render
from django.http import JsonResponse
from app_book.models import Book
from app_book.api.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def book_list(request):
    serializer = BookSerializer(Book.objects.all(), many=True)
    return Response(serializer.data)