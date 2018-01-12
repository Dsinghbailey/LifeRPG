from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Profile, Aspect

# Create your views here.


def home(request):
    return render(request, 'index.html', context={})


def register(request):
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


@login_required
def profile(request):
    if not Profile.objects.filter(user=request.user.id).exists():
        return redirect(levelup)
    profile = Profile.objects.filter(user=request.user.id)
    context = {'profile': profile}
    return render(request, 'profile.html', context)


@login_required
def levelup(request):
    aspects = Aspect.objects.all()
    context = {'aspects': aspects}
    return render(request, 'levelup.html', context)
