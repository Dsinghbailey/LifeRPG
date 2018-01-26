from django import forms
from .models import IntakeQuestion


class CreateProfileForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        choices = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]
        questions = IntakeQuestion.objects.all()
        for i, question in enumerate(questions):
            self.fields['q_%s' % i] = forms.ChoiceField(label=question.question,
                                                        widget=forms.RadioSelect(
                                                            attrs={'class': "with-gap"}),
                                                        choices=choices,
                                                        required=True)
