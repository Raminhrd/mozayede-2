from django.urls import path
from auction_app.views import *


urlpatterns = [
    path('create', AcutionCreate.as_view()),
    path('list', AuctionList.as_view()),
    path('offer/<pk>', OfferCreate.as_view()),
]