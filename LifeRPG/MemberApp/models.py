from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Mission(models.Model):
    image = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    science = models.CharField(max_length=200, null=True)


class Aspect(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=200, default='white')
    description = models.CharField(max_length=200, null=True)


class MissionAspect(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    aspect = models.ForeignKey(Aspect, on_delete=models.CASCADE)


class UserMissionRec(models.Model):
    rec_date = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    rank = models.IntegerField()


class UserMissionRating(models.Model):
    log_time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    rating = models.IntegerField()


class IntakeQuestion(models.Model):
    aspect = models.ForeignKey(Aspect, null=True, on_delete=models.SET_NULL)
    question = models.CharField(max_length=200)


class UserIntakeQuestion(models.Model):
    log_time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(IntakeQuestion, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    @property
    def aspect(self):
        aspect = self.question.aspect
        return aspect


class Profile(models.Model):
    log_time = models.DateTimeField(default=datetime.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.IntegerField(default=0)
    level = models.IntegerField()
    xp = models.IntegerField()
    hearts = models.IntegerField()

    @property
    def user_aspects(self):
        user_aspects = UserAspect.objects.filter(user=self.user)
        return user_aspects

    @property
    def user_focus(self):
        user_focus = UserFocus.objects.filter(user=self.user,
                                              level=self.level)
        aspects = []
        for focus in user_focus:
            aspect = focus.aspect
            aspects.append(aspect)
        return aspects


class UserAspect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aspect = models.ForeignKey(Aspect, on_delete=models.CASCADE)
    points = models.IntegerField()


class UserFocus(models.Model):
    log_time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField()
    aspect = models.ForeignKey(Aspect, null=True, on_delete=models.SET_NULL)
    slot = models.IntegerField()
