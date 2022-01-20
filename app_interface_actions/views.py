from django.shortcuts import render, redirect
from django.contrib import messages

from app_interface_actions.models import Interface_Actions
from app_interface_actions.forms import InterfaceActionsForm

from app_interface.models import Interface
from app_implementation.models import Implementation


def clone_interface(request, interface_id):
    if request.method == "POST":
        interface_actions_form = InterfaceActionsForm(request.POST or None)
        if interface_actions_form.is_valid():
            instance = interface_actions_form.save(commit=False)
            
            instance.save()
            messages.success(request, (f"Interface '{instance}' wurde erfolgreich gecloned."))
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
