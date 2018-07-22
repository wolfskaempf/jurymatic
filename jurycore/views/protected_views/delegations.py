from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from guardian.decorators import permission_required_or_403

from jurycore.forms import DelegationForm
from jurycore.models import Booklet, Delegation, Delegate

@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
def delegation_list(request, booklet):
    """ This view shows a list of all delegations of a given booklet"""
    booklet = get_object_or_404(Booklet, slug=booklet)
    delegations = Delegation.objects.filter(booklet=booklet).order_by("name")

    context = {"booklet": booklet, "delegations": delegations}
    template = "jurycore/delegations/delegation_list.html"
    return render(request, template, context)

@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
def delegation_show(request, booklet, uuid):
    """ This view shows an individual delegation and all its delegates formatted for printing """
    delegation = get_object_or_404(Delegation, uuid=uuid)
    booklet = get_object_or_404(Booklet, slug=booklet)

    if not delegation.booklet == booklet:
        return HttpResponseForbidden()

    delegates = Delegate.objects.filter(delegation=delegation).order_by("committee__name")

    context = {"delegation": delegation, "delegates": delegates, "delegation_show": True}
    template = "jurycore/delegations/delegation_show.html"
    return render(request, template, context)

@login_required()
@permission_required_or_403('change_booklet', (Booklet, 'slug', 'booklet'))
def delegation_create(request, booklet):
    """This view creates a delegation"""
    booklet = get_object_or_404(Booklet, slug=booklet)

    form = DelegationForm()
    if request.method == "POST":
        form = DelegationForm(request.POST)
        if form.is_valid():
            delegation = Delegation(name=form.cleaned_data['name'], colour=form.cleaned_data['colour'], booklet=booklet)
            delegation.save()
            messages.success(request, form.cleaned_data['name'] + ' has been added successfully.')
            form = DelegationForm()

    template = "jurycore/delegations/delegation_create.html"
    context = {"form": form, "booklet": booklet}
    return render(request, template, context)

@login_required()
@permission_required_or_403('change_booklet', (Booklet, 'slug', 'booklet'))
def delegation_update(request, booklet, uuid):
    """This view updates delegations"""
    booklet = get_object_or_404(Booklet, slug=booklet)
    delegation = get_object_or_404(Delegation, uuid=uuid)

    if not delegation.booklet == booklet:
        return HttpResponseForbidden()

    form = DelegationForm(instance=delegation)
    if request.method == "POST":
        form = DelegationForm(request.POST, instance=delegation)
        if form.is_valid():
            form.save()
            messages.success(request, form.cleaned_data['name'] + ' has been updated successfully.')
            return HttpResponseRedirect(reverse('jurycore:delegation_list', args=[booklet.slug]))

    template = "jurycore/delegations/delegation_update.html"
    context = {"form": form, "booklet": booklet}
    return render(request, template, context)


@login_required()
@permission_required_or_403('change_booklet', (Booklet, 'slug', 'booklet'))
def delegation_delete(request, booklet, uuid):
    """ This view deletes the delegation on POST """
    booklet = get_object_or_404(Booklet, slug=booklet)
    delegation = get_object_or_404(Delegation, uuid=uuid)

    if not delegation.booklet == booklet:
        return HttpResponseForbidden()

    if request.method == "POST":
        delegation.delete()
        messages.success(request, delegation.name + ' has been deleted successfully.')
        return HttpResponseRedirect(reverse('jurycore:delegation_list', args=[booklet.slug]))

    context = {"booklet": booklet, "delegation": delegation}
    template = "jurycore/delegations/delegation_delete.html"

    return render(request, template, context)
