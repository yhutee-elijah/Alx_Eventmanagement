from rest_framework import serializers
from .models import Event, User
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyFieldField(source='organizer.username')
    class Meta:
        model = Event
        fields = '__all__'
    def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Event date cannot be in the past.")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    