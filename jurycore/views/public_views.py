import uuid

from django.shortcuts import redirect, render

from jurycore.models import Booklet


def home(request):
    """ This view shows some basic information to help the user understand the software """
    booklets = Booklet.objects.all()
    for booklet in booklets:
        booklet.uuid = uuid.uuid4()
        booklet.save()
    if request.user.is_authenticated:
        return redirect('jurycore:dashboard')
    context = {}
    template = "jurycore/home.html"
    return render(request, template, context)
