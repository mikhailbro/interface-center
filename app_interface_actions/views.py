from django.shortcuts import render, redirect
from django.contrib import messages

from app_interface_actions.forms import InterfaceActionsForm
from app_interface.models import Interface
from app_review.models import Review
from app_implementation.models import Implementation


def quality_check(request, interface_id):
    interface_obj = Interface.objects.get(pk=interface_id)
    
    review_objs = Review.objects.all().filter(interface=interface_obj)
    implementation_objs = Implementation.objects.all().filter(interface=interface_obj)
    

    interface_status_owner = 'OK'
    if interface_obj.status != 'EINGANG':
        if interface_obj.owner.username != 'Administrator':
            interface_status_owner = f"Interface Status bereits {interface_obj.status}, obwohl Interface noch {interface_obj.owner.first_name} {interface_obj.owner.last_name} gehört"

    inteface_status_review = 'OK'
    if interface_obj.status != 'EINGANG':
        if len(review_objs) <= 0:
            inteface_status_review = f"Interface Status bereits {interface_obj.status}, obwohl es noch kein Review exisitert"
        else:
            for idx in range(len(review_objs)):
                if not review_objs[idx].review_status == 'DONE':
                    inteface_status_review = f"Interface Status bereits {interface_obj.status} obwohl es mindestens ein nicht abgeschlossenens Review exisitert"


    inteface_implementations = 'OK'
    if len(implementation_objs) <= 0:
        inteface_implementations = f"Interface Implementations fehlen"


    quality_check_obj = {
        'interface_status_owner': interface_status_owner,
        'interface_status_review': inteface_status_review,
        'inteface_implementations': inteface_implementations,
    }

    return render(request, 'quality_check.html', {'interface_obj': interface_obj, 'quality_check_obj': quality_check_obj})



def clone_interface(request, interface_id):
    if request.method == "POST":
        interface_actions_form = InterfaceActionsForm(request.POST or None)
        
        if interface_actions_form.is_valid():
            instance = interface_actions_form.save(commit=False)
            
            interface = Interface.objects.get(pk=interface_id)
            implementations = Implementation.objects.all().filter(interface=interface)

            # CLONE Interface:
            interface.pk = None
            interface.name = instance.name
            interface.interface_id = instance.interface_id
            interface.version = instance.version
            interface.description = instance.description
            interface.contract_description = instance.contract_description
            interface.created_at = instance.created_at
            interface.production_start_at = instance.production_start_at

             # validation:
            interface_validation = validation(interface)
            if len(interface_validation) > 0:
                messages.error(request, (interface_validation))
                return redirect('clone_interface', interface_id)

            else:    
                interface.save()

                # CLONE Implementations:
                for idx in range(len(implementations)):
                    implementations[idx].pk = None
                    implementations[idx].interface = interface
                    implementations[idx].provider_basepath = ''
                    implementations[idx].save()


                messages.success(request, (f"Interface wurde erfolgreich gecloned."))
                return redirect('index')

    else:
        # prefilling:
        interface = Interface.objects.get(pk=interface_id)
        
        init_interface_actions_form = {
            'name': interface.name,
            'interface_id': interface.interface_id,
            'version': interface.version, 
            'description': interface.description, 
        }

        interface_actions_obj = InterfaceActionsForm(request.POST or None, initial=init_interface_actions_form)
        return render(request, 'clone_interface.html', {'interface_actions_obj': interface_actions_obj, 'interface_obj': interface})



def validation(interface_obj):
    all_interfaces = Interface.objects.all()
    for idx in range(len(all_interfaces)):
        if all_interfaces[idx].name == interface_obj.name:
            return f"Ein Interface mit dem Namen '{interface_obj.name}' ist bereits vorhanden"
        
        if all_interfaces[idx].interface_id == interface_obj.interface_id:
            return f"Ein Interface mit der Interface ID '{interface_obj.interface_id}' ist bereits vorhanden"


    name_undescore_position = interface_obj.name.rfind("_")+1
    if name_undescore_position <= 0:
        return f"Interface Name '{interface_obj.name}' entspricht nicht den Namenskonventionen, s. Benutzeranleitung unten"

    name_version = interface_obj.name[name_undescore_position:]
    if int(name_version) != interface_obj.version:
       return f"Version im Interface Namen stimmt nicht mit der eigentlichen Interface Version überein: '{name_version}' und '{interface_obj.version}'"

    id_undescore_position = interface_obj.interface_id.find("_")+1
    if id_undescore_position <= 0:
        return f"Interface ID '{interface_obj.interface_id}' entspricht nicht den Namenskonventionen, s. Benutzeranleitung unten"

    id_version = interface_obj.interface_id[id_undescore_position:]
    if int(id_version) != interface_obj.version:
       return f"Version in der Interface ID stimmt nicht mit der eigentlichen Interface Version überein: '{id_version}' und '{interface_obj.version}'"   

    if interface_obj.created_at > interface_obj.production_start_at:
        return f"Produktivstellung kann nicht vor der Interface-Anlage stattfinden"
    
    return ''