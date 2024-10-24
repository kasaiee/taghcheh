from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


FORMAT_CHOICES = (
    ('pdf', 'pdf'),
    ('epub', 'epub'),
    ('mp3', 'mp3'),
)


class Publisher(models.Model):
    name = models.CharField(max_length=70, null=True)
    logo = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=70, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=70, null=True)
    description = models.TextField()
    author = models.ManyToManyField(User, related_name='books')
    translator = models.ManyToManyField(User, related_name='books_translated')
    narrator = models.ManyToManyField(User, related_name='books_narrated')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    price = models.PositiveIntegerField(default=0)
    format = models.CharField(default='pdf', choices=FORMAT_CHOICES, max_length=4)
    size = models.PositiveIntegerField(default=0)
    publish_date = models.DateField(null=True)
    page_count = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title