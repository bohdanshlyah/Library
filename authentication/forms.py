from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserAdminCreationForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        print('I am working')
        if commit:
            user.save()
        return user


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name',
                  'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name')
