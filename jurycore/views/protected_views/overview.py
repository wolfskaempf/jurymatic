from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from guardian.shortcuts import get_objects_for_user

from jurycore.models import Booklet


@login_required()
def dashboard(request):
    """ This view is an overview of the users booklets """

    booklets = get_objects_for_user(request.user, 'view_booklet', Booklet)

    context = {"booklets": booklets}
    template = "jurycore/dashboard.html"
    return render(request, template, context)
