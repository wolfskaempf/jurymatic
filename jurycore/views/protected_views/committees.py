from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from guardian.decorators import permission_required_or_403

from jurycore.models import Booklet, Committee, Delegate


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
def committee_list(request, booklet):
    """ This view shows a list of all committees of a given booklet"""
    booklet = get_object_or_404(Booklet, slug=booklet)
    committees = Committee.objects.filter(booklet=booklet).order_by("name")

    context = {"committees": committees}
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
