from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import get_objects_for_user, assign_perm

from jurycore.forms import DelegateForm, BookletForm
from jurycore.models import Committee, Delegate, Delegation, Booklet


@login_required()
def dashboard(request):
    """ This view is an overview of the users booklets """

    booklets = get_objects_for_user(request.user, 'view_booklet', Booklet)

    context = {"booklets": booklets}
    template = "jurycore/dashboard.html"
    return render(request, template, context)


@login_required()
def booklet_create(request):
    """ This view creates booklets """
    form = BookletForm()
    if request.method == "POST":
        form = BookletForm(request.POST)
        if form.is_valid():
            booklet = Booklet(session_name=form.cleaned_data['session_name'], created_by=request.user)
            booklet.save()
            assign_perm('view_booklet', request.user, booklet)
            assign_perm('change_booklet', request.user, booklet)
            assign_perm('delete_booklet', request.user, booklet)
            messages.success(request, form.cleaned_data['session_name'] + ' has been created successfully.')
            return HttpResponseRedirect(reverse('jurycore:booklet_show', args=[booklet.slug]))

    template = "jurycore/booklet_create.html"
    context = {"form": form}
    return render(request, template, context)


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'slug'))
def booklet_show(request, slug):
    """ This view shows the overview of a booklet """
    booklet = get_object_or_404(Booklet, slug=slug)
    committees = Committee.objects.filter(booklet=booklet)
    delegations = Delegation.objects.filter(booklet=booklet)

    context = {"booklet": booklet, "committees": committees, "delegations": delegations}
    template = "jurycore/booklet_show.html"

    return render(request, template, context)


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


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
def committee_list(request, booklet):
    """ This view shows a list of all committees of a given booklet"""
    booklet = get_object_or_404(Booklet, slug=booklet)
    committees = Committee.objects.filter(booklet=booklet).order_by("name")

    context = {"committees": committees}
    template = "jurycore/committee_list.html"
    return render(request, template, context)


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
@permission_required_or_403('view_committee', (Committee, 'uuid', 'uuid'))
def committee_show(request, booklet, uuid):
    """ This view shows an individual committee and all its delegates formatted for printing """

    committee = Committee.objects.get(uuid=uuid)

    delegates = Delegate.objects.filter(committee=committee)

    context = {"committee": committee, "delegates": delegates}
    template = "jurycore/committee_show.html"
    return render(request, template, context)


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
@permission_required_or_403('view_delegation', (Delegation, 'uuid', 'uuid'))
def delegation_show(request, booklet, uuid):
    """ This view shows an individual delegation and all its delegates formatted for printing """
    delegation = Delegation.objects.get(uuid=uuid)

    delegates = Delegate.objects.filter(delegation=delegation).order_by("committee__name")

    context = {"delegation": delegation, "delegates": delegates, "delegation_show": True}
    template = "jurycore/delegation_show.html"
    return render(request, template, context)


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
def printing_view(request, booklet):
    """ This view lists all committees and all delegates at the same time, formatted for printing """
    booklet = Booklet.objects.get(slug=booklet)
    committees = Committee.objects.filter(booklet=booklet).order_by("name")

    context = {"committees": committees}
    template = "jurycore/printing_view.html"
    return render(request, template, context)
