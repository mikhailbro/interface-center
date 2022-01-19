from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_implementation.models import Implementation
from app_implementation.forms import ImplementationForm
from app_interface.models import Interface
from app_interface.forms import InterfaceForm
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
def create_implementation(request, interface_id):
    if request.method == "POST":
        implementation_form = ImplementationForm(request.POST or None)
        if implementation_form.is_valid():
            instance = implementation_form.save(commit=False)
            interface = request.POST.get('interface')
            provider = request.POST.get('provider')

            # validation:
            implementation_validation = validation(instance, interface)
            if len(implementation_validation) > 0:
                messages.error(request, (implementation_validation))
                return redirect('create_implementation', interface)

            else:
                # automatic assignment:
                instance.implementation_counter = create_implementation_counter(interface, provider)

                instance.save()

                messages.success(request, (f"Implementation '{instance}' wurde erfolgreich angelegt"))
                return redirect('update_interface', interface)
    else:
        interface = Interface.objects.get(pk=interface_id)
            
        # prefilling:
        init_implementation_form = {
            'interface': interface, 
            'provider': interface.owner_application,
            'implementation_type': interface.interface_type,
        }
        
        implementation_form = ImplementationForm(request.POST or None, initial=init_implementation_form)
        return render(request, 'create_implementation.html', {'implementation_obj': implementation_form, 'interface_obj':interface})

def create_implementation_counter(interface_obj, application_obj):
    interface_implementations = Implementation.objects.all().filter(interface=interface_obj).filter(provider=application_obj)
    return str(len(interface_implementations) + 1)


@login_required
def update_implementation(request, implementation_id):
    if request.method == "POST":
        implementation = Implementation.objects.get(pk=implementation_id)
        implementation_form = ImplementationForm(request.POST or None, instance = implementation)
        if implementation_form.is_valid():
            instance = implementation_form.save(commit=False)
            interface = request.POST.get('interface')
                
            # validation:
            implementation_validation = validation(instance, interface)
            if len(implementation_validation) > 0:
                messages.error(request, (implementation_validation))
                return redirect('update_implementation', interface)
                
            else:
                implementation.consumers.set([])
                for consumer in implementation_form.cleaned_data['consumers']:
                    implementation.consumers.add(consumer)
                
                instance.save()

                messages.success(request, (f"Implementation '{instance}' wurde erfolgreich aktualisiert"))
                return redirect('update_interface', interface)
    else:
        implementation = Implementation.objects.get(pk=implementation_id)
        implementation_form = ImplementationForm(request.POST or None, instance = implementation)
        return render(request, 'update_implementation.html', {'implementation_obj': implementation_form, 'interface': implementation.interface})



def validation(implementation_obj, interface_id):
    result = ''
    interface = Interface.objects.get(pk=interface_id)

    if not interface.multi_provider:
        if interface.owner_application != implementation_obj.provider:
            result = f"Interface '{interface}' ist kein Multi-Provider Interface! Es darf nur Application '{interface.owner_application}' als Implementation Provider deklariert werden!"

    return result

