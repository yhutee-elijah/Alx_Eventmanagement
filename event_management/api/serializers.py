from rest_framework import serializers
from .models import Event, Category, Registration, Comment
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_time', 'location', 'capacity', 'created_date', 'organizer']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    event = serializers.ReadOnlyField(source='event.id')

    class Meta:
        model = Registration
        fields = ['id', 'user', 'event', 'registered_at']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'event', 'content', 'created_at']        
