from django.contrib import admin
from .models import Event, Category, Registration, Comment

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Registration)
admin.site.register(Comment)
