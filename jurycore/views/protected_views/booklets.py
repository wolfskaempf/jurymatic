from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import assign_perm

from jurycore.forms import BookletForm
from jurycore.models import Booklet, Committee, Delegation, Delegate


@login_required()
def booklet_create(request):
    """ This view creates booklets """
    form = BookletForm()
    if request.method == "POST":
        form = BookletForm(request.POST)
        if form.is_valid():
            booklet = form.save(False)
            booklet.created_by = request.user
            booklet.save()
            assign_perm('view_booklet', request.user, booklet)
            assign_perm('change_booklet', request.user, booklet)
            assign_perm('delete_booklet', request.user, booklet)
            messages.success(request, form.cleaned_data['session_name'] + ' has been created successfully.')
            return HttpResponseRedirect(reverse('jurycore:booklet_show', args=[booklet.slug]))

    template = "jurycore/booklets/booklet_create.html"
    context = {"form": form}
    return render(request, template, context)


@login_required()
@permission_required_or_403('view_booklet', (Booklet, 'slug', 'slug'))
def booklet_show(request, slug):
    """ This view shows the overview of a booklet """
    booklet = get_object_or_404(Booklet, slug=slug)
    committees = Committee.objects.filter(booklet=booklet)
    delegations = Delegation.objects.filter(booklet=booklet)

    statistics = {
        'delegate_count': Delegate.objects.filter(booklet=booklet).count(),
        'committee_count': committees.count(),
        'delegation_count': delegations.count()
    }

    context = {"booklet": booklet, "committees": committees, "delegations": delegations, "statistics": statistics}
    template = "jurycore/booklets/booklet_show.html"

    return render(request, template, context)


@login_required()
@permission_required_or_403('change_booklet', (Booklet, 'slug', 'slug'))
def booklet_update(request, slug):
    """This view updates a booklet"""
    booklet = get_object_or_404(Booklet, slug=slug)

    form = BookletForm(instance=booklet)
    if request.method == "POST":
        form = BookletForm(request.POST, instance=booklet)
        if form.is_valid():
            form.save()
            messages.success(request, form.cleaned_data['session_name'] + ' has been updated successfully.')
            return HttpResponseRedirect(reverse('jurycore:booklet_show', args=[booklet.slug]))

    template = "jurycore/booklets/booklet_update.html"
    context = {"form": form, "booklet": booklet}
    return render(request, template, context)


@login_required()
@permission_required_or_403('delete_booklet', (Booklet, 'slug', 'slug'))
def booklet_delete(request, slug):
    """ This view deletes the booklet on POST """
    booklet = get_object_or_404(Booklet, slug=slug)

    if request.method == "POST":
        booklet.delete()
        messages.success(request, booklet.session_name + ' has been deleted successfully.')
        return HttpResponseRedirect(reverse('jurycore:dashboard'))

    context = {"booklet": booklet}
    template = "jurycore/booklets/booklet_delete.html"

    return render(request, template, context)
