from django import forms


class CreateProfileForm(forms.Form):
    choices = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]
    questions = [
        "I feel the sleep I get is adequate and I wake feeling rested.",
        "I eat regular nutritious meals that give me the energy I need to get through the day.",
        "I get a total of 150 minutes (2 ½ hrs.) of moderate to vigorous physical activity per week (e.g. brisk walking, bike riding, jogging).",
        "I’m able to find the time to maintain healthy relationships with friends and family.",
        "I feel I belong to a group or community.",
        "I respect others and their cultural identities.",
        "I feel optimistic about my academic program and career goals.",
        "I feel satisfied with my school and career performance.",
        "I seek out new challenges related to my academic and career goals.",
        "I feel an overall sense of peace and well-being in my life.",
        "I am aware of my own values and beliefs, and respect the values and beliefs of others.",
        "I believe my life is meaningful and has direction.",
        "I care for and respect the environment and the community.",
        "I am aware of the risks within my environment and make adjustments to my lifestyle accordingly (e.g. travel health, personal safety).",
        "I try to live an eco-friendly lifestyle (e.g. buying local food, driving less, turning the lights off).",
        "I develop financial plans to manage my long term goals.",
        "I budget my spending each month.",
        "I have enough money to manage my living needs.",
        "I’m able to ask for/seek help when I need it - from friends, family, or professionals.",
        "I value self-exploration and self-improvement.",
        "I am able to recognize and manage the different stressors in my life."
    ]
    q0 = forms.ChoiceField(label=questions[0],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q1 = forms.ChoiceField(label=questions[1],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q2 = forms.ChoiceField(label=questions[2],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q3 = forms.ChoiceField(label=questions[3],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q4 = forms.ChoiceField(label=questions[4],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q5 = forms.ChoiceField(label=questions[5],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q6 = forms.ChoiceField(label=questions[6],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q7 = forms.ChoiceField(label=questions[7],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q8 = forms.ChoiceField(label=questions[8],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q9 = forms.ChoiceField(label=questions[9],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q10 = forms.ChoiceField(label=questions[10],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q11 = forms.ChoiceField(label=questions[11],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q12 = forms.ChoiceField(label=questions[12],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q13 = forms.ChoiceField(label=questions[13],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q14 = forms.ChoiceField(label=questions[14],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q15 = forms.ChoiceField(label=questions[15],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q16 = forms.ChoiceField(label=questions[16],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q17 = forms.ChoiceField(label=questions[17],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q18 = forms.ChoiceField(label=questions[18],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q19 = forms.ChoiceField(label=questions[19],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
    q20 = forms.ChoiceField(label=questions[20],
                           widget=forms.RadioSelect(
                               attrs={'class': "with-gap"}),
                           choices=choices,
                           required=True)
