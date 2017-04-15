from django.core.management.base import BaseCommand, CommandError

from goshort.models import ShortenURL

class Command(BaseCommand):
    help = 'refreshes all short urls'

    def handle(self, *args, **options):
        return ShortenURL.objects.refresh_shorturls()
