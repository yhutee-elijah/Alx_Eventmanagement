from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

urlpatterns = [
    path('api/auth/', include('events.urls')),
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('api/', include('api.urls')),  # API endpoints
    path('accounts/', include('django.contrib.auth.urls')), # Login/logout
    path('accounts/', include('users.urls')),  # User registration
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]