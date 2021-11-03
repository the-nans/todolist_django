import random

from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()
        names = ['ann', 'bob', 'tim', 'kate', 'serge']
        lastnames = ['doe', 'smith', 'tailor', 'thomson', 'hu']
        login_flavs = ['kitty', '2001', 'washere', 'cool', 'name']
        random.shuffle(names)
        random.shuffle(lastnames)
        random.shuffle(login_flavs)
        for i in range(0, 5):
            new_user = User.objects.create_user(username=f'{names[i]}{login_flavs[i]}',
                                                     first_name=f'{names[i]}',
                                                     last_name=f'{lastnames[i]}',
                                                     email=f'{names[i]}_{lastnames[i]}@box.ru',
                                                     password=f'pass123-{i}')
            new_user.save()

        User.objects.create_superuser(username='root', password='rootpass')