from rest_framework import serializers
from .models import Menu, Offer, Booking, Feedback

class MenuSerializers(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('id', 'name', 'price', 'category')

class OfferSerializers(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('id', 'title', 'expiry_date', 'description')

class BookingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('name', 'contact', 'email', 'date', 'remark')

class FeedbackSerializers(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ('name', 'feedback', 'email', 'rating')
