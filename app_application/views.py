from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_application.models import Application
from app_application.forms import ApplicationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def applications(request):
    # ALL APPLICATIONS:
    all_applications = Application.objects.all()
    # Pagination:
    paginator_all_applications = Paginator(all_applications, 10)
    page = request.GET.get('pg')
    all_applications = paginator_all_applications.get_page(page)

    return render(request, 'applications.html', {'applications': all_applications})


@login_required
def details(request, application_id):
    if request.method == "POST":
        application = Application.objects.get(pk=application_id)
        form = ApplicationForm(request.POST or None, instance = application)
        if form.is_valid():
            form.save()

        messages.success(request, (f"Application '{application.shortname}' is successfully updated!"))
        return redirect('applications')
    else:
        application_obj = Application.objects.get(pk=application_id)
        return render(request, 'details.html', {'application_obj': application_obj})