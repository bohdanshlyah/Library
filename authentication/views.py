from django.contrib.auth import authenticate, login, views, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, render, resolve_url, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib import messages

from .forms import CreateUserForm, LoginUserForm, UpdateUserForm
from .models import CustomUser


def auth(request):
    context = {
        'form': LoginUserForm(),
        'signup_form': CreateUserForm(),
    }
    return render(request, 'registration/login.html', context=context)
    

class UserLoginView(views.LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return resolve_url('index')
    
    def get_redirect_url(self):
        return resolve_url('auth:auth')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('index')
    return render(request, 'registration/login.html', 
                    context={ 'form': LoginUserForm(),
                              'signup_form': form,
                              'flag': True
                              })

class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'registration/user_list.html'

    def test_func(self):
        return self.request.user.role == 1

class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'registration/profile.html'

    def get_object(self, **kwargs):
        return get_object_or_404(CustomUser, id=self.request.user.id)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UpdateUserForm
    template_name = 'registration/update_user.html'
    model = CustomUser

    def get_success_url(self):
        messages.success(self.request, 'Your info was updated successfully!')
        return reverse('auth:user_profile', kwargs={'pk': self.request.user.pk})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('auth:user_profile', pk=user.pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })