from django.shortcuts import render

# Create your views here.

from .models import Committee, Delegate, Delegation

def home(request):
    """ This view shows some basic information to help the user understand the software """
    committees = Committee.objects.all()

    context = {"committees": committees}
    template = "jurycore/home.html"
    return render(request, template, context)

def committee_list(request):
    """ This view shows a list of all committees"""
    committees = Committee.objects.all()

    context = {"committees": committees}
    template = "jurycore/committee_list.html"
    return render(request, template, context)

def committee_show(request, pk):
    """ This view shows an individual committee and all its delegates formatted for printing """
    committee = Committee.objects.get(pk=pk)

    delegates = Delegate.objects.filter(committee_id=pk)

    context = {"committee": committee, "delegates": delegates}
    template = "jurycore/committee_show.html"
    return render(request, template, context)

def printing_view(request):
    """ This view lists all committees and all delegates at the same time, formatted for printing """
    committees = Committee.objects.all()

    context = {"committees": committees}
    template = "jurycore/printing_view.html"
    return render(request, template, context)
