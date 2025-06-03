from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Создает суперпользователя только если он не существует'

    def handle(self, *args, **options):
        User = get_user_model()
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='qwerty123'
            )
            self.stdout.write(
                self.style.SUCCESS('Суперпользователь admin создан успешно!')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Суперпользователь admin уже существует')
            ) 