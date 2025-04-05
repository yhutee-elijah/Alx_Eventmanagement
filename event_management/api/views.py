from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, serializers
from .serializers import EventSerializer, UserSerializer
from events.models import Event
from django.contrib.auth.models import User
from .permissions import IsOrganizerOrReadOnly
from django.utils.timezone import now
from events.models import Category, Registration, Comment
from .serializers import CategorySerializer, RegistrationSerializer, CommentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Category View
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Comment View
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(event__id=self.kwargs['event_pk'])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, event_id=self.kwargs['event_pk'])

# Event Registration View
class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(event__id=self.kwargs['event_pk'])

    def perform_create(self, serializer):
        event = Event.objects.get(id=self.kwargs['event_pk'])
        if event.is_full():
            raise serializers.ValidationError("Event is full.")
        serializer.save(user=self.request.user, event=event)


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOrganizerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'location']
    ordering_fields = ['date_time']
    
    def get_queryset(self):
        # List only upcoming events
        queryset = Event.objects.filter(date_time__gt=now()).order_by('date_time')
        title = self.request.query_params.get('title')
        location = self.request.query_params.get('location')
        if title:
            queryset = queryset.filter(title__icontains=title)
        if location:
            queryset = queryset.filter(location__icontains=location)
        return queryset

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

