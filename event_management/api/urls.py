from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import EventViewSet, UserViewSet,  CategoryViewSet, RegistrationViewSet, CommentViewSet
 

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)

events_router = NestedDefaultRouter(router, r'events', lookup='event')
events_router.register(r'registrations', RegistrationViewSet, basename='event-registrations')
events_router.register(r'comments', CommentViewSet, basename='event-comments')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(events_router.urls)),                    
]
