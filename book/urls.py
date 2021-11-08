from django.urls import path
from . import views


app_name = 'book'

urlpatterns = [
    path('', views.BookList.as_view(), name='books_list'),
	path('<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
	path('create/', views.BookCreate.as_view(), name='book_create'),
	path('update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
	path('delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
]

