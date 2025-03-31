from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    help = 'Displays a welcome message'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help="Provide your name", required=False)

    def handle(self, *args: Any, **options: Any):
        name = options.get('name', 'User')
        self.stdout.write(self.style.SUCCESS(f'Processing {name}...'))
