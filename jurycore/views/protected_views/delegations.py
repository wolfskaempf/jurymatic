from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from guardian.decorators import permission_required_or_403

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
