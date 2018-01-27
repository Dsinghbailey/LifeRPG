from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile, Aspect, UserAspect, IntakeQuestion,\
    UserIntakeQuestion, Mission, UserMissionRatings
from .forms import CreateProfileForm, MissionRatingForm
import datetime


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def create_profile(request):
    init_profile(request)
    profile = Profile.objects.get(user=request.user)
    if(profile.created == 1):
        return redirect('tutorial')
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            # Add answers to UserIntakeQuestion
            answers = list(form.cleaned_data.values())
            questions = IntakeQuestion.objects.all()
            now = datetime.datetime.now()
            for i, question in enumerate(questions):
                user_reply = UserIntakeQuestion(user=request.user,
                                                question=question,
                                                value=answers[i],
                                                log_time=now)
                user_reply.save()
            user_replies_to_stats(request.user)
            profile.created = 1
            profile.save()
            return redirect('tutorial')
    else:
        form = CreateProfileForm()
    context = {'profile': profile, 'form': form}
    return render(request, 'create_profile.html', context)


@login_required
def tutorial(request):
    if check_profile_redirect(request):
        return redirect('create_profile')
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'tutorial.html', context)


@login_required
def profile(request):
    if check_profile_redirect(request):
            return redirect('create_profile')
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'profile.html', context=context)


@login_required
def levelup(request):
    if check_profile_redirect(request):
        return redirect('create_profile')
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile, 'max_points': 3}
    return render(request, 'levelup.html', context=context)


@login_required
def missions(request):
    if check_profile_redirect(request):
            return redirect('create_profile')
    return render(request, 'missions.html', {'missions': range(5)})


@login_required
def mission_review(request):
    if check_profile_redirect(request):
        return redirect('create_profile')
    if request.method == 'POST':
        form = MissionRatingForm(request.POST)
        if form.is_valid():
            # Add answers to UserIntakeQuestion
            now = datetime.datetime.now()
            rating = list(form.cleaned_data.values())[0]
            mission = Mission(image='d', title='d', content='d', science='f')
            mission.save()
            mission_rating = UserMissionRatings(log_time=now,
                                                user=request.user,
                                                rating=rating,
                                                mission=mission)
            mission_rating.save()
            return redirect('missions')
    else:
        form = MissionRatingForm()
    context = {'profile': profile, 'form': form}
    return render(request, 'mission_review.html', context)


#  Utility functions
def check_profile_redirect(request):
        if Profile.objects.filter(user=request.user).exists():
            return False
        else:
            return True


def init_profile(request):
        if not Profile.objects.filter(user=request.user).exists():
            Profile.objects.create(user=request.user, level=0,
                                   xp=0, hearts=3)
            aspects = Aspect.objects.all()
            for aspect in aspects:
                UserAspect.objects.create(user=request.user,
                                          aspect=aspect,
                                          points=0)


def user_replies_to_stats(user):
    user_replies = UserIntakeQuestion.objects.filter(user=user)
    for reply in user_replies:
        user_aspect = UserAspect.objects.get(user=user, aspect=reply.aspect)
        user_aspect.points += reply.value
        user_aspect.save()
