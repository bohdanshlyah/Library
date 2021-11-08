from django.shortcuts import render, redirect, reverse, resolve_url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Author


class AuthorList(UserPassesTestMixin, ListView):
    model = Author
    template_name = 'authors_list.html'

    def test_func(self):
        return self.request.user.role == 1


class AuthorCreate(UserPassesTestMixin, CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = '__all__'

    def test_func(self):
        return self.request.user.role == 1

    def form_valid(self, form):
        #  author = self.request.author
        #  form.instance.author = author
         return super(AuthorCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('authors_list')


class AuthorDelete(UserPassesTestMixin, DeleteView):
    model = Author
    template_name = 'author_delete.html'

    def test_func(self):
        return self.request.user.role == 1

    def get_success_url(self):
        return reverse('authors_list')


class AuthorUpdate(UserPassesTestMixin, UpdateView):
    model = Author
    template_name = 'author_update.html'
    fields = '__all__'

    def test_func(self):
        return self.request.user.role == 1

    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author_details.html'