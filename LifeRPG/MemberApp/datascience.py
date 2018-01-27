from .models import Mission
from random import randint
import pdb

MISSIONS_PER_DAY = 5


def get_user_missions(num=MISSIONS_PER_DAY):
    missions = []
    for i in range(num):
        missions.append(get_rand_mission())
    return missions


def get_rand_mission():
    count = Mission.objects.all().count()
    random_index = randint(0, count - 1)
    return Mission.objects.all()[random_index]
