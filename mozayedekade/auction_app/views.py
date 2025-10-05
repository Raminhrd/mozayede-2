from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from user_app.permissions import IsNotBanUser
from rest_framework import permissions
from auction_app.serializer import*
from rest_framework.exceptions import ValidationError
from auction_app.models import *



class AuctionList(ListAPIView):
    permission_classes = [permissions.IsAuthenticated,IsNotBanUser]
    queryset = Auctions.objects.filter(is_closed=False)
    serializer_class = AuctionCreateListSerializer


class AcutionCreate(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Auctions.objects.all()
    serializer_class = AuctionDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(current_price = serializer.validated_data['start_price'], is_closed=False)


class OfferCreate(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        auction = Auctions.objects.get(pk=pk)
        amount = int(self.request.data.get('amount'))
        

        if auction.is_closed:
            raise ValidationError({'error': 'auction is not avaliable'})
        if amount < auction.current_price:
            raise ValidationError({'error': 'amount is too low'})
        serializer.save(user = self.request.user.userprofile, auction=auction)
        auction.current_price = amount
        auction.winner = self.request.user.userprofile
        auction.save()
        auction.close()