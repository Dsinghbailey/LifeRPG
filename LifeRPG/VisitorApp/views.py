from django.shortcuts import render, redirect
from MemberApp.views import profile
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def home(request):
    if request.user.is_authenticated():
        return redirect(profile)
    return render(request, 'index.html', context={})


def contact(request):
    return render(request, 'contact.html', context={})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

