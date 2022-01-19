from django.shortcuts import render, redirect
from django.http import HttpResponse

from app_interface.models import Interface
from app_interface.forms import InterfaceForm
from app_implementation.models import Implementation
from app_implementation.forms import ImplementationForm
from app_review.models import Review
from app_review.forms import ReviewForm
from app_application.models import Application


from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request):
    # ALL INTERFACES:
    query = request.GET.get('q')
    if not query:
        query = ''
    if query == '':
        all_interfaces = Interface.objects.all()
    else:
        all_interfaces = Interface.objects.filter(Q(interface_id__icontains=query) | Q(name__icontains=query) | Q(status__icontains=query) | Q(interface_type__icontains=query) | Q(contract_description__icontains=query) | Q(description__icontains=query))
    
    counter = all_interfaces.__len__

    # Pagination:
    paginator_all_interfaces = Paginator(all_interfaces, 25)
    page = request.GET.get('pg')
    all_interfaces = paginator_all_interfaces.get_page(page)

    return render(request, 'index.html', {'interfaces': all_interfaces, 'counter': counter})
    

def interface_details(request, interface_id):
    interface_obj = Interface.objects.get(pk=interface_id)

    review_objs = Review.objects.all().filter(interface=interface_obj)
    implementation_objs = Implementation.objects.all().filter(interface=interface_obj)

    return render(request, 'interface.html', {'interface_obj': interface_obj, 'implementation_objs': implementation_objs, 'review_objs': review_objs})


@login_required
def my_interfaces(request):
    if request.method == "POST":
        form = InterfaceForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request, ("Interface '{instance}' wurde erfolgreich gespeichert"))
        else: 
            messages.error(request, ("Interface konnte nicht gespeichert werden!"))
        return redirect('my_interfaces')
    else:
        # MY INTERFACES:
        query = request.GET.get('q')
        if not query:
            query = ''
        if query == '':
            my_interfaces = Interface.objects.filter(owner=request.user)
        else:
            my_interfaces = Interface.objects.filter(Q(interface_id__icontains=query) | Q(name__icontains=query) | Q(status__icontains=query) | Q(interface_type__icontains=query) | Q(contract_description__icontains=query) | Q(description__icontains=query)).filter(owner=request.user)

        counter = my_interfaces.__len__

        # Pagination:
        paginator_my_interfaces = Paginator(my_interfaces, 25)
        page = request.GET.get('pg')
        my_interfaces = paginator_my_interfaces.get_page(page)

        return render(request, 'my_interfaces.html', {'interfaces': my_interfaces, 'counter': counter})


@login_required
def create_interface(request):
    if request.method == "POST":
        interface_form = InterfaceForm(request.POST or None)
        if interface_form.is_valid():
            instance = interface_form.save(commit=False)
            
            # validation:
            interface_validation = validation(instance)
            if len(interface_validation) > 0:
                messages.error(request, (interface_validation))
                return redirect('create_interface')

            else:    
                # automatic assignment:
                if instance.owned_interface:
                    if instance.interface_type == "FILE_TRANSFER":
                        instance.interface_id = create_interface_id('T', instance.version, instance.name)
                    else:
                        instance.interface_id = create_interface_id('S', instance.version, instance.name)
                else:
                    instance.interface_id = create_interface_id('X', instance.version, instance.name)

                instance.save()
                messages.success(request, (f"Interface '{instance}' wurde erfolgreich angelegt. Implementations sollen direkt im Interface eingetragen werden."))
                return redirect('my_interfaces')
    else:
        # prefilling:
        init_implementation_form = {
            'owner': request.user
        }
        
        interface_obj = InterfaceForm(request.POST or None, initial=init_implementation_form)
        return render(request, 'create_interface.html', {'interface_obj': interface_obj})


def create_interface_id(type, version, name):
    all_interfaces = Interface.objects.all()
    max_existing_id = 1
    for idx in range(len(all_interfaces)):
        if all_interfaces[idx].interface_id.startswith(type):
            prefix = int(all_interfaces[idx].interface_id[1:5])
            if prefix >= max_existing_id:
                max_existing_id = prefix + 1

            undescore_position = name.find("_")
            if all_interfaces[idx].name.startswith(name[0:undescore_position]):
                max_existing_id = prefix
                break

    max_existing_id_str = str(max_existing_id).zfill(4)
    version_str = str(version).zfill(3)

    return f"{type}{max_existing_id_str}_{version_str}"



@login_required
def update_interface(request, interface_id):
    if request.method == "POST":
        interface = Interface.objects.get(pk=interface_id)
        interface_form = InterfaceForm(request.POST or None, instance = interface)
        if interface_form.is_valid():
            instance = interface_form.save(commit=False)

            # validation:
            interface_validation = validation(interface)
            if len(interface_validation) > 0:
                messages.error(request, (interface_validation))
                return redirect('update_interface', interface_id)

            else:    
                instance.save()
                messages.success(request, (f"Interface '{instance}' wurde erfolgreich aktualisiert"))
                return redirect('my_interfaces')
    else:
        interface = Interface.objects.get(pk=interface_id)
        interface_form = InterfaceForm(request.POST or None, instance = interface)

        review_objs = Review.objects.all().filter(interface=interface)
        implementation_objs = Implementation.objects.all().filter(interface=interface)

        return render(request, 'update_interface.html', {'interface_obj': interface_form, 'implementation_objs': implementation_objs, 'review_objs': review_objs, 'interface_id': interface_id})


def validation(interface_obj):
    result = ''
    
    if interface_obj.restriction:
        if (interface_obj.restriction_code is None or len(interface_obj.restriction_code.strip()) == 0 or interface_obj.restriction_text is None or len(interface_obj.restriction_text.strip()) == 0):
            result = f"Bitte trage Restriction Code und Restriction Text ein, falls eine Restriction gewünscht ist"

    if not interface_obj.restriction:
        if ((not interface_obj.restriction_code is None and len(interface_obj.restriction_code.strip()) > 0) or (not interface_obj.restriction_text is None and len(interface_obj.restriction_text.strip()) > 0)):
            result = f"Bitte deklariere eine Restriction zu Restriction Code und Restriction Text ein, falls eine Restriction gewünscht ist"

    return result