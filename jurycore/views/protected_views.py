from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from jurycore.forms import DelegateForm
from jurycore.models import Committee, Delegate, Delegation, Booklet


def home(request):
    """ This view shows some basic information to help the user understand the software """

    context = {}
    template = "jurycore/home.html"
    return render(request, template, context)


@login_required()
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
def committee_list(request):
    """ This view shows a list of all committees"""
    committees = Committee.objects.all().order_by("name")

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
