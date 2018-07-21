from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import get_objects_for_user

from jurycore.forms import DelegateForm
from jurycore.models import Committee, Delegate, Delegation, Booklet


def home(request):
    """ This view shows some basic information to help the user understand the software """
    if request.user.is_authenticated:
        return redirect('jurycore:dashboard')
    context = {}
    template = "jurycore/home.html"
    return render(request, template, context)


@login_required()
def dashboard(request):
    """ This view is an overview of the users booklets """

    booklets = get_objects_for_user(request.user, 'view_booklet', Booklet)

    context = {"booklets": booklets}
    template = "jurycore/dashboard.html"
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
    """ This view shows a list of all committees"""
    booklet = get_object_or_404(Booklet, slug=booklet)
    committees = Committee.objects.filter(booklet=booklet).order_by("name")

    context = {"committees": committees}
    template = "jurycore/committee_list.html"
    return render(request, template, context)


@login_required()
def committee_show(request, pk):
    """ This view shows an individual committee and all its delegates formatted for printing """
    committee = Committee.objects.get(pk=pk)

    delegates = Delegate.objects.filter(committee_id=pk)

    context = {"committee": committee, "delegates": delegates}
    template = "jurycore/committee_show.html"
    return render(request, template, context)


@login_required()
def delegation_show(request, pk):
    """ This view shows an individual delegation and all its delegates formatted for printing """
    delegation = Delegation.objects.get(pk=pk)

    delegates = Delegate.objects.filter(delegation_id=pk).order_by("committee__name")

    context = {"delegation": delegation, "delegates": delegates, "delegation_show": True}
    template = "jurycore/delegation_show.html"
    return render(request, template, context)


@login_required()
def printing_view(request):
    """ This view lists all committees and all delegates at the same time, formatted for printing """
    committees = Committee.objects.all().order_by("name")

    context = {"committees": committees}
    template = "jurycore/printing_view.html"
    return render(request, template, context)
