from django.urls import path
from app_review import views as review_views


urlpatterns = [
    path('', review_views.reviews, name='reviews'),
    path('review/<review_id>', review_views.review_details, name='review_details'),
    path('create_implementation', review_views.create_review, name='create_review'),
    path('update_implementation', review_views.update_review, name='update_review'),
]