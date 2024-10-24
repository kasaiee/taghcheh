from django.contrib import admin
from app_book.models import Publisher, Category, Book

admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Book)