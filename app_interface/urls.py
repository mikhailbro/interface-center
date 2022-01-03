from django.urls import path
from app_interface import views as interface_views
from app_user import views as users_views


urlpatterns = [
    path('', interface_views.my_interfaces, name='my_interfaces'),
    path('delete/<interface_id>', interface_views.delete_interface, name='delete_interface'),
    path('edit/<interface_id>', interface_views.edit_interface, name='edit_interface'),
    path('view/<interface_id>', interface_views.view_interface, name='view_interface'),
    path('complete/<interface_id>', interface_views.complete_interface, name='complete_interface'),
    path('pending/<interface_id>', interface_views.pending_interface, name='pending_interface'),
]