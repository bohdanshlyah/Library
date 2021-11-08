from django.urls import path
from django.conf.urls import include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.AuthorList.as_view(), name='authors_list'),
	path('<int:pk>', views.AuthorDetail.as_view(), name='author_detail'),
	path('create/', views.AuthorCreate.as_view(), name='author_create'),
	path('update/<int:pk>', views.AuthorUpdate.as_view(), name='author_update'),
	path('delete/<int:pk>', views.AuthorDelete.as_view(), name='author_delete'),
]