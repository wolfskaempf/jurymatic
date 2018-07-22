from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from guardian.decorators import permission_required_or_403

from jurycore.forms import CommitteeForm
from jurycore.models import Booklet, Committee, Delegate


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
def committee_list(request, booklet):
    """ This view shows a list of all committees of a given booklet"""
    booklet = get_object_or_404(Booklet, slug=booklet)
    committees = Committee.objects.filter(booklet=booklet).order_by("name")

    context = {"booklet": booklet, "committees": committees}
    template = "jurycore/committees/committee_list.html"
    return render(request, template, context)


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
@permission_required_or_403('view_committee', (Committee, 'uuid', 'uuid'))
def committee_show(request, booklet, uuid):
    """ This view shows an individual committee and all its delegates formatted for printing """

    committee = Committee.objects.get(uuid=uuid)

    delegates = Delegate.objects.filter(committee=committee)

    context = {"committee": committee, "delegates": delegates}
    template = "jurycore/committees/committee_show.html"
    return render(request, template, context)

@login_required()
@permission_required_or_403('change_booklet', (Booklet, 'slug', 'booklet'))
def committee_create(request, booklet):
    """This view creates delegates"""
    booklet = get_object_or_404(Booklet, slug=booklet)
    form = CommitteeForm()
    if request.method == "POST":
        form = CommitteeForm(request.POST, request.FILES)
        if form.is_valid():
            committee = Committee(name=form.cleaned_data['name'], booklet=booklet)
            committee.save()
            messages.success(request, form.cleaned_data['name'] + ' has been added successfully.')
            form = CommitteeForm()

    template = "jurycore/committees/committee_create.html"
    context = {"form": form, "booklet": booklet}
    return render(request, template, context)