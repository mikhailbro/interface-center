from django.urls import path
from app_implementation import views as implementation_views


urlpatterns = [
    path('', implementation_views.implementations, name='implementations'),
    path('details/<implementation_id>', implementation_views.details, name='implementation_details'),

]