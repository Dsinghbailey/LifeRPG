from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile, Aspect, UserAspect, IntakeQuestion,\
    UserIntakeQuestion, Mission, UserMissionRating, UserFocus,\
    UserMissionRec
from .forms import CreateProfileForm, MissionRatingForm, LevelUpForm
import datetime
from AdminApp.tasks import rec_user_missions

MAX_XP = 100


# Views
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def create_profile(request):
    if(Profile.objects.filter(user=request.user).exists()):
        profile = Profile.objects.get(user=request.user)
        if(profile.created == 1):
            return redirect('tutorial')

    init_profile(request)
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            # Add answers to UserIntakeQuestion
            answers = list(form.cleaned_data.values())
            questions = IntakeQuestion.objects.all()
            for i, question in enumerate(questions):
                user_reply = UserIntakeQuestion(user=request.user,
                                                question=question,
                                                value=answers[i])
                user_reply.save()
            user_replies_to_stats(request.user)
            profile.created = 1
            profile.save()
            return redirect('levelup')
    else:
        form = CreateProfileForm()
    context = {'profile': profile, 'form': form}
    return render(request, 'create_profile.html', context)


@login_required
def tutorial(request):
    if create_profile_redirect(request):
        return redirect('create_profile')
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'tutorial.html', context)


@login_required
def profile(request):
    if create_profile_redirect(request):
            return redirect('create_profile')
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'profile.html', context=context)


@login_required
def levelup(request):
    if create_profile_redirect(request):
        return redirect('create_profile')
    profile = Profile.objects.get(user=request.user)
    if profile.xp < MAX_XP:
        redirect('profile')
    if request.method == 'POST':
        form = LevelUpForm(request.POST)
        if form.is_valid():
            # level up
            profile.level += 1
            profile.xp = 0
            profile.save()
            # save user_focus
            focii = list(form.cleaned_data.values())
            for slot, focus in enumerate(focii):
                aspect = Aspect.objects.get(name=focus)
                user_focus = UserFocus(user=request.user,
                                       level=profile.level,
                                       aspect=aspect,
                                       slot=slot)
                user_focus.save()

            # If first level show tutorial
            if profile.level == 1:
                return redirect('tutorial')
            else:
                return redirect('profile')
    else:
        form = LevelUpForm()
    context = {'profile': profile, 'form': form}
    return render(request, 'levelup.html', context=context)


@login_required
def missions(request):
    if create_profile_redirect(request):
            return redirect('create_profile')
    rec_user_missions()
    recs = UserMissionRec.objects.filter(user=request.user,
                                         rec_date=datetime.date.today())
    return render(request, 'missions.html',
                  {'recs': recs})


@login_required
def mission_review(request):
    if create_profile_redirect(request):
        return redirect('create_profile')
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = MissionRatingForm(request.POST)
        if form.is_valid():
            # Add answers to UserIntakeQuestion
            rating = list(form.cleaned_data.values())[0]
            try:
                mission_id = request.GET["id"]
            except:
                return redirect('missions')
            mission = Mission.objects.get(id=mission_id)
            mission.save()
            # Save MissionRating
            mission_rating = UserMissionRating(user=request.user,
                                               rating=rating,
                                               mission=mission)
            mission_rating.save()
            # Add xp to profile
            # TODO: should xp change by mission?
            profile.xp += profile.hearts
            profile.save()
            if profile.xp < MAX_XP:
                return redirect('missions')
            else:
                return redirect('levelup')
    else:
        form = MissionRatingForm()
    context = {'profile': profile, 'form': form}
    return render(request, 'mission_review.html', context)


#  Utility functions
def create_profile_redirect(request):
        if Profile.objects.filter(user=request.user).exists():
            return False
        else:
            return True


def init_profile(request):
        if not Profile.objects.filter(user=request.user).exists():
            Profile.objects.create(user=request.user,
                                   level=0,
                                   # Start with levelup
                                   xp=MAX_XP,
                                   hearts=3)
        aspects = Aspect.objects.all()
        for aspect in aspects:
            if not UserAspect.objects.filter(user=request.user,
                                             aspect=aspect).exists():
                UserAspect.objects.create(user=request.user,
                                          aspect=aspect,
                                          points=0)


def user_replies_to_stats(user):
    user_replies = UserIntakeQuestion.objects.filter(user=user)
    for reply in user_replies:
        user_aspect = UserAspect.objects.get(user=user, aspect=reply.aspect)
        user_aspect.points += reply.value
        user_aspect.save()
