from django.forms import ModelForm
from models import UserLevelUps


class LevelUpForm(ModelForm):
    class Meta:
        model = UserLevelUps
        fields = ['user', 'level', 'aspect', 'points']
