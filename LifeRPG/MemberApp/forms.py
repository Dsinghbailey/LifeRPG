from django import forms
from .models import IntakeQuestion

choices = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]


class CreateProfileForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        questions = IntakeQuestion.objects.all()
        for i, question in enumerate(questions):
            color = question.aspect.color
            self.fields['q_%s' % i] = forms.ChoiceField(label=question.question,
                                                        widget=forms.RadioSelect(),
                                                        # Store color in helptext
                                                        help_text=color,
                                                        choices=choices,
                                                        required=True)


class MissionRatingForm(forms.Form):
    rating = forms.ChoiceField(label='To finish the mission please rate it.',
                               widget=forms.RadioSelect(),
                               choices=choices,
                               required=True)


class LevelUpForm(forms.Form):
    slot1 = forms.CharField(required=True,
                            error_messages={'required': ''})
    slot2 = forms.CharField(required=True,
                            error_messages={'required': ''})
    slot3 = forms.CharField(required=True,
                            error_messages={'required': 'You left a slot blank'})
