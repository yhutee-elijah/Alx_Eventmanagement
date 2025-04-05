from django.contrib import admin
from .models import User  # Assuming you have a custom User model defined in models.py

admin.site.register(User)  # Register the custom User model with the admin site