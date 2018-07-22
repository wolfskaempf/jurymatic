from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def sign_up(request):
    """ This view creates a user """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('jurycore:dashboard')
    else:
        form = UserCreationForm()
    context = {"form": form}
    template = "registration/sign_up.html"
    return render(request, template, context)
