from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_implementation.models import Implementation
from app_implementation.forms import ImplementationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def implementations(request):
    # ALL IMPLEMENTATIONS:
    all_implementations = Implementation.objects.all()
    # Pagination:
    paginator_all_implementations = Paginator(all_implementations, 10)
    page = request.GET.get('pg')
    all_implementations = paginator_all_implementations.get_page(page)

    return render(request, 'implementations.html', {'implementations': all_implementations})


def implementation_details(request, implementation_id):
    implementation_obj = Implementation.objects.get(pk=implementation_id)
    return render(request, 'implementation.html', {'implementation_obj': implementation_obj})


@login_required
def create_implementation(request):
    if request.method == "POST":
        implementation_form = ImplementationForm(request.POST or None)
        if implementation_form.is_valid():
            instance = implementation_form.save(commit=False)
            interface = request.POST.get('interface')
            instance.save()

            messages.success(request, (f"Implementation is successfully created"))
            return redirect('update_interface', interface)
    else:
        implementation_form = ImplementationForm(request.POST or None)
        return render(request, 'create_implementation.html', {'implementation_obj': implementation_form})


@login_required
def update_implementation(request, implementation_id):
    if request.method == "POST":
        implementation = Implementation.objects.get(pk=implementation_id)
        implementation_form = ImplementationForm(request.POST or None, instance = implementation)
        if implementation_form.is_valid():
            instance = implementation_form.save(commit=False)
            interface = request.POST.get('interface')
            instance.save()

            messages.success(request, (f"Implementation is successfully updated"))
            return redirect('update_interface', interface)
    else:
        implementation = Implementation.objects.get(pk=implementation_id)
        implementation_form = ImplementationForm(request.POST or None, instance = implementation)
        return render(request, 'update_implementation.html', {'implementation_obj': implementation_form, 'interface': implementation.interface})

