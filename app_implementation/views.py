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


@login_required
def details(request, implementation_id):
    if request.method == "POST":
        implementation = Implementation.objects.get(pk=implementation_id)
        form = ImplementationForm(request.POST or None, instance = implementation)
        if form.is_valid():
            form.save()

        messages.success(request, (f"Implementation '{implementation.shortname}' is successfully updated!"))
        return redirect('implementations')
    else:
        implementation_obj = Implementation.objects.get(pk=implementation_id)
        return render(request, 'details.html', {'implementation_obj': implementation_obj})