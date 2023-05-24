from django import forms
from .models import *
import re


class TeamSearch(forms.Form):
    name = forms.CharField(label='Поиск по названию', required=False, help_text='Поиск по названию Команды',
                           max_length=255)

    def clean_name(self):
        name = self.cleaned_data['name']

        if re.search(r'[^\d\sa-zA-Z]', name):
            raise forms.ValidationError('Имя не должно содержать "9"!')
        return name


class TeamAdd(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].empty_label = 'не выбрана'

    class Meta:
        model = Team
        fields = ('name', 'country', 'rating')


