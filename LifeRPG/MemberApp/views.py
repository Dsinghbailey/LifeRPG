from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile, Aspect, UserAspect
from .forms import CreateProfileForm


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def create_profile(request):
    if not Profile.objects.filter(user=request.user).exists():
        Profile.objects.create(user=request.user, level=0,
                               xp=0, hearts=3)
        aspects = Aspect.objects.all()
        for aspect in aspects:
            UserAspect.objects.create(user=request.user,
                                      aspect=aspect,
                                      points=0)
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        print('hey2')
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            return redirect('tutorial')
    else:
        print('hey')
        form = CreateProfileForm()
    context = {'profile': profile, 'form': form}
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
