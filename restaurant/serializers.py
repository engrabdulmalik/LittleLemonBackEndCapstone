from rest_framework import serializers
from .models import Booking, Menu


class bookingSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = '__all__'


class menuSerializer(serializers.Serializer):
    class Meta:
        model = Menu
        fields = '__all__'
