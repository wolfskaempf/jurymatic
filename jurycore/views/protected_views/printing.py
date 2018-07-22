from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from guardian.decorators import permission_required_or_403

from jurycore.models import Booklet, Committee


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'booklet'))
def printing_view(request, booklet):
    """ This view lists all committees and all delegates at the same time, formatted for printing """
    booklet = Booklet.objects.get(slug=booklet)
    committees = Committee.objects.filter(booklet=booklet).order_by("name")

    context = {"committees": committees}
    template = "jurycore/printing_view.html"
    return render(request, template, context)
