from django import forms
from django.forms import ModelForm
from .models import Author


class CreateAuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')
        success_url = '/authors'