from django.urls import path
from app_interface_actions import views as interface_actions_views

urlpatterns = [
    path('clone_interface/<interface_id>', interface_actions_views.clone_interface, name='clone_interface'),
]