from django.urls import path
from app_implementation import views as implementation_views


urlpatterns = [
    #path('', implementation_views.implementations, name='implementations'),
    path('implementation/<implementation_id>', implementation_views.implementation_details, name='implementation_details'),
    path('create_implementation', implementation_views.create_implementation, name='create_implementation'),
    path('update_implementation', implementation_views.update_implementation, name='update_implementation'),
]