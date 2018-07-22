from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from guardian.decorators import permission_required_or_403

from jurycore.forms import DelegateForm
from jurycore.models import Booklet, Committee, Delegation


@login_required()
@permission_required_or_403('change_booklet', (Booklet, 'slug', 'booklet'))
def delegate_create(request, booklet):
    """This view create a delegate"""
    booklet = get_object_or_404(Booklet, slug=booklet)
    form = DelegateForm()
    form.fields['committee'].queryset = Committee.objects.filter(booklet=booklet)
    form.fields['delegation'].queryset = Delegation.objects.filter(booklet=booklet)

    if request.method == "POST":
        form = DelegateForm(request.POST, request.FILES)
        if form.is_valid():
            delegate = form.save(False)
            delegate.booklet = booklet
            delegate.save()
            messages.success(request, form.cleaned_data['name'] + ' has been added successfully.')
            form = DelegateForm()

    template = "jurycore/delegates/delegate_create.html"
    context = {"form": form, "booklet": booklet}
    return render(request, template, context)
