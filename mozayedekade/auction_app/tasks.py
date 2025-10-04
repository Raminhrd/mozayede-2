from celery import shared_task
from django.utils import timezone
from .models import Auctions



@shared_task(bind=True)
def check_auctions(self):
    now = timezone.now()
    auctions = Auctions.objects.filter(is_closed=False)

    for auction in auctions:
        if auction.end_time <= now or auction.current_price >= auction.target_price:
            auction.close()