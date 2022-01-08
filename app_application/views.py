from django.shortcuts import render, redirect
from app_application.models import Application
from app_application.forms import ApplicationForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def applications(request):
    query = request.GET.get('q')
    if not query:
        query = ''
    if query == '':
        all_applications = Application.objects.all()
    else:
        all_applications = Application.objects.filter(Q(short_name__icontains=query) | Q(app_id__icontains=query) | Q(mail_address__icontains=query))

    # Pagination:
    paginator_all_applications = Paginator(all_applications, 10)
    page = request.GET.get('pg')
    all_applications = paginator_all_applications.get_page(page)

    return render(request, 'applications.html', {'applications': all_applications})


def details(request, application_id):
    application_obj = Application.objects.get(pk=application_id)
    return render(request, 'application.html', {'application_obj': application_obj})