from django.shortcuts import redirect, render


def home(request):
    """ This view shows some basic information to help the user understand the software """
    if request.user.is_authenticated:
        return redirect('jurycore:dashboard')
    context = {}
    template = "jurycore/home.html"
    return render(request, template, context)