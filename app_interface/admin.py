from django.contrib import admin
from app_interface.models import Interface
from app_implementation.models import Implementation
from app_application.models import Application
from app_review.models import Review

# Register your models here.
admin.site.register(Interface)