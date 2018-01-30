from MemberApp.models import Mission, UserMissionRec
from django.contrib.auth.models import User
from celery import shared_task
import numpy as np

MISSIONS_PER_DAY = 5

 
# Tasks
def rec_user_missions(num=MISSIONS_PER_DAY):
    for user in User.objects.all():
        rec_rand_missions(user, num)


# Utility
def rec_rand_missions(user, num):
    count = Mission.objects.all().count()
    ids = np.random.choice(a=count,
                           size=num,
                           replace=False)
    for idx, val in enumerate(ids):
        mission = (Mission.objects.all()[int(val)])
        rec = UserMissionRec(user=user,
                             mission=mission,
                             rank=idx)
        rec.save()
