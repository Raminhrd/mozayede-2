from django.db import models
from user_app.models import UserProfile
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=100)


class Auctions(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    start_price = models.PositiveBigIntegerField()
    current_price = models.PositiveBigIntegerField()
    target_price = models.PositiveBigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    winner = models.ForeignKey(to= UserProfile, on_delete=models.SET_NULL, null=True , blank=True)
    is_closed = models.BooleanField(default=False)
    end_time = models.DateTimeField()
    last_offer = models.DateTimeField(null=True , blank=True)


    def close(self):
        if self.is_closed:
            return False
        if timezone.now() >= self.end_time or self.current_price >= self.target_price:
            self.is_closed = True
            self.save()
            return True
        return self.is_closed

class Offer(models.Model):
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    auction = models.ForeignKey(to=Auctions, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveBigIntegerField()