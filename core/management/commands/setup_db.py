from django.core.management.base import BaseCommand
from django.core.management import call_command
import sys


class Command(BaseCommand):
    help = 'Setup database with safe migrations'

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS('🚀 Starting database setup...'))
            
            # Выполняем миграции с timeout
            call_command('migrate', verbosity=1)
            
            self.stdout.write(self.style.SUCCESS('✅ Database setup completed!'))
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Database setup failed: {str(e)}')
            )
            sys.exit(1) 