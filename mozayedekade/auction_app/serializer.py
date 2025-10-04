from rest_framework.serializers import ModelSerializer, StringRelatedField
from auction_app.models import *


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class AuctionCreateListSerializer(ModelSerializer):
    class Meta:
        model = Auctions
        fields = [
            'id',
            'title',
            'start_price',
            'current_price',
            'target_price',
            'end_time',
            'is_closed'
        ]


class AuctionDetailSerializer(ModelSerializer):
    winner = StringRelatedField()

    class Meta:
        model = Auctions
        fields = [
            'id',
            'title',
            'description',
            'start_price',
            'current_price',
            'target_price',
            'end_time',
            'is_closed',
            'winner',
            'create_at',
            'last_offer'
        ]
        

class OfferSerializer(ModelSerializer):
    user = StringRelatedField()
    auction = StringRelatedField()

    class Meta:
        model = Offer
        fields = ['id', 'user', 'auction', 'amount', 'create_at']