from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_review.models import Review
from app_review.forms import ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def reviews(request):
    # ALL REVIEWS:
    all_reviews = Review.objects.all()
    # Pagination:
    paginator_all_reviews = Paginator(all_reviews, 10)
    page = request.GET.get('pg')
    all_reviews = paginator_all_reviews.get_page(page)

    return render(request, 'reviews.html', {'reviews': all_reviews})


@login_required
def review_details(request, review_id):
    if request.method == "POST":
        review = Review.objects.get(pk=review_id)
        form = ReviewForm(request.POST or None, instance = review)
        if form.is_valid():
            form.save()

        messages.success(request, (f"Review '{review.shortname}' is successfully updated!"))
        return redirect('reviews')
    else:
        review_obj = Review.objects.get(pk=review_id)
        return render(request, 'review.html', {'review_obj': review_obj})


@login_required
def create_review(request):
    return render(request, 'create_review.html')


@login_required
def update_review(request):
    return render(request, 'update_review.html')