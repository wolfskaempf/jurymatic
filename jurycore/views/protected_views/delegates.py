from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from guardian.decorators import permission_required_or_403

from jurycore.forms import DelegateForm
from jurycore.models import Booklet, Committee, Delegation, Delegate


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
def delegate_list(request, booklet):
    """ This view shows a list of all delegates of a given booklet"""
    booklet = get_object_or_404(Booklet, slug=booklet)
    delegates = Delegate.objects.filter(booklet=booklet).order_by("name")

    context = {"booklet": booklet, "delegates": delegates}
    template = "jurycore/delegates/delegate_list.html"
    return render(request, template, context)


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


@login_required()
@permission_required_or_403('change_booklet', (Booklet, 'slug', 'booklet'))
def delegate_update(request, booklet, uuid):
    """This view updates a delegate """
    booklet = get_object_or_404(Booklet, slug=booklet)
    delegate = get_object_or_404(Delegate, uuid=uuid)

    if not delegate.booklet == booklet:
        return HttpResponseForbidden()

    form = DelegateForm(instance=delegate)
    form.fields['committee'].queryset = Committee.objects.filter(booklet=booklet)
    form.fields['delegation'].queryset = Delegation.objects.filter(booklet=booklet)

    if request.method == "POST":
        form = DelegateForm(request.POST, request.FILES, instance=delegate)
        if form.is_valid():
            form.save()
            messages.success(request, form.cleaned_data['name'] + ' has been renamed successfully.')
            return HttpResponseRedirect(reverse('jurycore:delegate_list', args=[booklet.slug]))

    template = "jurycore/delegates/delegate_update.html"
    context = {"form": form, "booklet": booklet}
    return render(request, template, context)


@login_required()
@permission_required_or_403('change_booklet', (Booklet, 'slug', 'booklet'))
def delegate_delete(request, booklet, uuid):
    """ This view deletes the delegate on POST """
    booklet = get_object_or_404(Booklet, slug=booklet)
    delegate = get_object_or_404(Delegate, uuid=uuid)

    if not delegate.booklet == booklet:
        return HttpResponseForbidden()

    if request.method == "POST":
        delegate.delete()
        messages.success(request, delegate.name + ' has been deleted successfully.')
        return HttpResponseRedirect(reverse('jurycore:delegate_list', args=[booklet.slug]))

    context = {"booklet": booklet, "delegate": delegate}
    template = "jurycore/delegates/delegate_delete.html"

    return render(request, template, context)
