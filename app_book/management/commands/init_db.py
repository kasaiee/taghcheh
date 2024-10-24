from tqdm import tqdm
from random import choice, randint
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from app_book.models import Book, Publisher, Category


PASSWORD = 'asdf@1234'
User = get_user_model()
format_choices = ['pdf', 'epub', 'mp3']

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        User.objects.all().delete()
        Book.objects.all().delete()
        Publisher.objects.all().delete()
        Category.objects.all().delete()

        User.objects.create_superuser(username='admin', password=PASSWORD)

        users = []
        for i in tqdm(range(1, 10), 'Creating users'):
            user = User.objects.create_user(username=f'user{i}', password=PASSWORD)
            users.append(user)
        
        publishers = []
        for i in tqdm(range(1, 6), 'Creating publishers'):
            publisher = Publisher.objects.create(name=f'publisher{i}')
            publishers.append(publisher)

        categories = []
        for i in tqdm(range(1, 11), 'Creating categories'):
            category = Category.objects.create(name=f'category{i}')
            categories.append(category)

        for i in tqdm(range(1, 51), 'Creating Books'):
            book = Book(
                title=f'book{i}',
                description=f'this is book{i} description',
                publisher=choice(publishers),
                price=randint(100, 1000),
                format=choice(format_choices),
                size=randint(3, 10),
                publish_date=timezone.now(),
                page_count=randint(50, 1000),
                duration=randint(100, 300)
            )
            book.save()
            book.author.add(choice(users))
            book.translator.add(choice(users))
            book.narrator.add(choice(users))
            book.category.add(choice(categories))
            book.save()
        