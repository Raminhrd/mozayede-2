from django.contrib import admin
from auction_app.models import *
from user_app.models import UserProfile


admin.site.register(Auctions)
admin.site.register(Company)
admin.site.register(Offer)
admin.site.register(UserProfile)