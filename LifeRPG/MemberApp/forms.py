from django import forms
from .models import IntakeQuestion

choices = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]


class CreateProfileForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        questions = IntakeQuestion.objects.all()
        for i, question in enumerate(questions):
            self.fields['q_%s' % i] = forms.ChoiceField(label=question.question,
                                                        widget=forms.RadioSelect(
                                                            attrs={'class': "with-gap"}),
                                                        choices=choices,
                                                        required=True)


class MissionRatingForm(forms.Form):
    rating = forms.ChoiceField(label='To finish the mission please rate it from 1 to 5.',
                               widget=forms.RadioSelect(
                                attrs={'class': "with-gap"}),
                               choices=choices,
                               required=True)

    
