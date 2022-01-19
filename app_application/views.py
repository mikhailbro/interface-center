from django.shortcuts import render, redirect
from app_application.models import Application
from app_interface.models import Interface
from app_implementation.models import Implementation
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
    
    counter = all_applications.__len__

    # Pagination:
    paginator_all_applications = Paginator(all_applications, 10)
    page = request.GET.get('pg')
    all_applications = paginator_all_applications.get_page(page)

    return render(request, 'applications.html', {'applications': all_applications, 'counter': counter})


def details(request, application_id):
    application_obj = Application.objects.get(pk=application_id)
    owned_interface_objs = search_owned_interfaces(application_obj)
    provided_implementation_objs = search_provided_implementations(application_obj)
    consumed_implementation_objs = search_consumed_implementations(application_obj)


    return render(request, 'application.html', {'application_obj': application_obj, 'owned_interface_objs': owned_interface_objs, 'provided_implementation_objs': provided_implementation_objs, 'consumed_implementation_objs': consumed_implementation_objs})

def search_owned_interfaces(application_obj):
    interface_objs = Interface.objects.filter(owner_application=application_obj)
    return interface_objs

def search_provided_implementations(application_obj):
    implementation_objs = Implementation.objects.filter(provider=application_obj)
    return implementation_objs

def search_consumed_implementations(application_obj):
    implementation_objs = Implementation.objects.filter(consumers=application_obj)
    return implementation_objs