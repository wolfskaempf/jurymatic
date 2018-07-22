from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from guardian.decorators import permission_required_or_403

from jurycore.forms import DelegationForm
from jurycore.models import Booklet, Delegation, Delegate


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
@permission_required_or_403('view_delegation', (Delegation, 'uuid', 'uuid'))
def delegation_show(request, booklet, uuid):
    """ This view shows an individual delegation and all its delegates formatted for printing """
    delegation = Delegation.objects.get(uuid=uuid)

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
def committee_update(request, booklet, uuid):
    """This view creates delegates"""
    booklet = get_object_or_404(Booklet, slug=booklet)
    committee = get_object_or_404(Committee, uuid=uuid)

    if not committee.booklet == booklet:
        return HttpResponseForbidden()

    form = CommitteeForm(instance=committee)
    if request.method == "POST":
        form = CommitteeForm(request.POST, instance=committee)
        if form.is_valid():
            form.save()
            messages.success(request, form.cleaned_data['name'] + ' has been renamed successfully.')
            return HttpResponseRedirect(reverse('jurycore:committee_list', args=[booklet.slug]))

    template = "jurycore/committees/committee_update.html"
    context = {"form": form, "booklet": booklet}
    return render(request, template, context)


@login_required()
@permission_required_or_403('change_booklet', (Booklet, 'slug', 'booklet'))
def committee_delete(request, booklet, uuid):
    """ This view deletes the committee on POST """
    booklet = get_object_or_404(Booklet, slug=booklet)
    committee = get_object_or_404(Committee, uuid=uuid)

    if not committee.booklet == booklet:
        return HttpResponseForbidden()

    if request.method == "POST":
        committee.delete()
        messages.success(request, booklet.session_name + ' has been deleted successfully.')
        return HttpResponseRedirect(reverse('jurycore:committee_list', args=[booklet.slug]))

    context = {"booklet": booklet, "committee": committee}
    template = "jurycore/committees/committee_delete.html"

    return render(request, template, context)
