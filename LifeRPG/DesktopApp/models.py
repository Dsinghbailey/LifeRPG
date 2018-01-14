from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Mission(models.Model):
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    #  Unused
    science = models.CharField(max_length=200)


class Aspect(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)


class MissionAspects(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    aspect = models.ForeignKey(Aspect, on_delete=models.CASCADE)


class UserMissionRatings(models.Model):
    log_time = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    rating = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField()
    xp = models.IntegerField()
    hearts = models.IntegerField()

    @property
    def aspects(self):

        return list(self.friends.all())


class UserAspects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aspect = models.ForeignKey(Aspect, on_delete=models.CASCADE)
    points = models.IntegerField()


class UserLevelUps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    levelup_time = models.DateField()
    level = models.IntegerField()
    aspect = models.ForeignKey(Aspect, null=True, on_delete=models.SET_NULL)
