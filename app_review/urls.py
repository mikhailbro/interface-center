from django.urls import path
from app_review import views as review_views


urlpatterns = [
    path('', review_views.reviews, name='reviews'),
    path('review/<review_id>', review_views.details, name='review_details'),

]