from django.shortcuts import render, redirect, resolve_url, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Book


class BookList(UserPassesTestMixin, ListView):
    model = Book
    template_name = 'books_list.html'

    def test_func(self):
        return self.request.user.role == 1


class BookCreate(UserPassesTestMixin, CreateView):
    model = Book
    template_name = 'book_create.html'
    fields = '__all__'

    def test_func(self):
        return self.request.user.role == 1

    def form_valid(self, form):
        #  book = self.request.book
        #  form.instance.book = book
         return super(BookCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('book:books_list')

class BookDelete(UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'

    def test_func(self):
        return self.request.user.role == 1

    def get_success_url(self):
        return reverse('book:books_list')


class BookUpdate(UserPassesTestMixin, UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = '__all__'

    def test_func(self):
        return self.request.user.role == 1

    def get_success_url(self):
        return reverse('book:book_detail', kwargs={'pk': self.object.pk})


class BookDetail(DetailView):
    model = Book
    template_name = 'book_details.html'
