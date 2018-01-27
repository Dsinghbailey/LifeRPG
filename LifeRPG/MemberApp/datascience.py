from .models import Mission
import numpy as np


MISSIONS_PER_DAY = 5


def get_user_missions(num=MISSIONS_PER_DAY):
    missions = get_rand_missions(num)
    return missions


def get_rand_missions(num):
    count = Mission.objects.all().count()
    ids = np.random.choice(a=count, size=num,
                           replace=False)
    missions = []
    for idx in ids:
        missions.append(Mission.objects.all()[int(idx)])

    return missions
