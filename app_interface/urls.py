from django.urls import path
from app_interface import views as interface_views
from app_user import views as users_views


urlpatterns = [
    path('', interface_views.my_interfaces, name='my_interfaces'),
    path('interface/<interface_id>', interface_views.interface_details, name='interface_details'),
    path('update_interface/<interface_id>', interface_views.update_interface, name='update_interface'),
    path('create_interface', interface_views.create_interface, name='create_interface'),
    
    path('delete/<interface_id>', interface_views.delete_interface, name='delete_interface'),
    path('complete/<interface_id>', interface_views.complete_interface, name='complete_interface'),
    path('pending/<interface_id>', interface_views.pending_interface, name='pending_interface'),
]