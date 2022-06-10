from django.urls import path, include
from app_interface import views as interface_views


urlpatterns = [
    path('my_interfaces', interface_views.my_interfaces, name='my_interfaces'),
    path('interface/<interface_id>', interface_views.interface_details, name='interface_details'),
    path('update_interface/<interface_id>', interface_views.update_interface, name='update_interface'),
    path('create_interface', interface_views.create_interface, name='create_interface'),
]