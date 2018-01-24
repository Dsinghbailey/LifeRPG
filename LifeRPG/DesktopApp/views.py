from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile, Aspect, UserAspect


def home(request):
    if request.user.is_authenticated():
        return redirect(profile)
    return render(request, 'index.html', context={})


def logout_view(request):
    logout(request)
    return redirect('home')


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


@login_required
def create_profile(request):
    if not Profile.objects.filter(user=request.user).exists():
        Profile.objects.create(user=request.user, level=0,
                               xp=0, hearts=3)
        aspects = Aspect.objects.all()
        for aspect in aspects:
            UserAspect.objects.create(user=request.user, aspect=aspect,
                                      points=0)
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'create_profile.html', context)


@login_required
def tutorial(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'tutorial.html', context)


@login_required
def profile(request):
    if not Profile.objects.filter(user=request.user).exists():
        return redirect(create_profile)
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'profile.html', context=context)


@login_required
def levelup(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile, 'max_points': 3}
    return render(request, 'levelup.html', context=context)


@login_required
def missions(request):
    if not Profile.objects.filter(user=request.user).exists():
        return redirect(create_profile)
    return render(request, 'missions.html', {'missions': range(5)})
