from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie  # model name to be edited
        fields = ['name', 'desc', 'year', 'image']
