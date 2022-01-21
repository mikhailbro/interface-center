from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_review.models import Review
from app_review.forms import ReviewForm
from app_interface.models import Interface
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


def review_details(request, review_id):
    review_obj = Review.objects.get(pk=review_id)
    return render(request, 'review.html', {'review_obj': review_obj})


@login_required
def create_review(request, interface_id):
    if request.method == "POST":
        review_form = ReviewForm(request.POST or None)
        if review_form.is_valid():
            instance = review_form.save(commit=False)
            interface = request.POST.get('interface')
            instance.save()

            messages.success(request, (f"Review is successfully created"))
            return redirect('interface_details', interface)
    else:
        interface = Interface.objects.get(pk=interface_id)

        # prefilling:
        init_review_form = {
            'interface': interface, 
            'requestor': interface.owner,
            'reviewer': request.user,
        }

        review_form = ReviewForm(request.POST or None, initial=init_review_form)
        return render(request, 'create_review.html', {'review_obj': review_form, 'interface_obj': interface})


@login_required
def update_review(request, review_id):
    if request.method == "POST":
        review = Review.objects.get(pk=review_id)
        review_form = ReviewForm(request.POST or None, instance = review)
        if review_form.is_valid():
            instance = review_form.save(commit=False)
            interface = request.POST.get('interface')
            instance.save()

            messages.success(request, (f"Review is successfully updated"))
            return redirect('review_details', review_id)
    else:
        review = Review.objects.get(pk=review_id)
        review_form = ReviewForm(request.POST or None, instance = review)
        return render(request, 'update_review.html', {'review_obj': review_form, 'interface_obj': review.interface})
