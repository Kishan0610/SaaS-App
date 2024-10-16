from typing import Any
from django.core.management.base import BaseCommand

from subscriptions.models import Subscription
from subscriptions import utils as sub_utils

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        sub_utils.sync_subs_group_permissions()