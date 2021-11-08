from django.urls import path
# from django.conf.urls import include
from django.contrib.auth.views import LogoutView
# from django.conf import settings
from . import views

app_name = 'auth'

urlpatterns = [
    path('', views.auth, name='auth'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='user_profile'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('user/', views.UserListView.as_view(), name='user_list'),
    path('password/', views.change_password, name='change_password'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
]
