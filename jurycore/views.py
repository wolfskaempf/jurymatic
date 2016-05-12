from django.shortcuts import render

# Create your views here.

from .models import Committee, Delegate, Delegation


def committee_list(request):
    """ This view shows a list of all committees"""
    committees = Committee.objects.all()

    context = {"committees": committees}
    template = "jurycore/committee_list.html"
    return render(request, template, context)
