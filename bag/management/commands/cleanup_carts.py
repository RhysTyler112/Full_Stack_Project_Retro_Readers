from django.core.management.base import BaseCommand
from django.contrib.sessions.models import Session
from bag.models import Cart, CartItem
from books.models import Books
import json


class Command(BaseCommand):
    help = 'Clean up old carts and sessions'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=30,
            help='Delete carts older than this many days (default: 30)',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without actually deleting',
        )

    def handle(self, *args, **options):
        from django.utils import timezone
        from datetime import timedelta

        days = options['days']
        dry_run = options['dry_run']
        cutoff_date = timezone.now() - timedelta(days=days)

        # Find old anonymous carts
        old_anonymous_carts = Cart.objects.filter(
            user__isnull=True,
            updated_at__lt=cutoff_date
        )

        # Find old empty carts
        old_empty_carts = Cart.objects.filter(
            updated_at__lt=cutoff_date,
            items__isnull=True
        )

        total_carts = old_anonymous_carts.count() + old_empty_carts.count()

        if dry_run:
            self.stdout.write(
                self.style.WARNING(
                    f'DRY RUN: Would delete {total_carts} old carts'
                )
            )
            self.stdout.write(
                f'- {old_anonymous_carts.count()} anonymous carts older than {days} days'
            )
            self.stdout.write(
                f'- {old_empty_carts.count()} empty carts older than {days} days'
            )
        else:
            old_anonymous_carts.delete()
            old_empty_carts.delete()
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully deleted {total_carts} old carts'
                )
            )