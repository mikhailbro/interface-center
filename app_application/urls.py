from django.urls import path
from app_interface import views as interface_views
from app_application import views as application_views
from app_user import views as users_views


urlpatterns = [
    path('', application_views.applications, name='applications'),
    path('application/<application_id>', application_views.details, name='application_details'),

]