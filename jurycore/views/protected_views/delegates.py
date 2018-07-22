from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from jurycore.forms import DelegateForm


@login_required()
def delegate_create(request):
    """This view creates delegates"""
    form = DelegateForm()
    if request.method == "POST":
        form = DelegateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(True)
            messages.success(request, form.cleaned_data['name'] + ' has been added successfully.')
            form = DelegateForm()

    template = "jurycore/delegate_create.html"
    context = {
        "form": form
    }
    return render(request, template, context)