from rest_framework import serializers
from .models import MenuItems, Booking
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['url', 'username', 'email', 'groups']



class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'