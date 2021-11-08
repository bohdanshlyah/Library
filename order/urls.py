from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', views.OrderList.as_view(), name='order_list'),
    path('<int:pk>/', views.OrderDetailView.as_view(),  name='order_detail'),
    path('update/<int:pk>/', views.OrderUpdateView.as_view(),  name='order_update'),
    path('delete/<int:pk>/', views.OrderDeleteView.as_view(),  name='order_delete'),
    path('create/', views.OrderCreateView.as_view(),  name='order_create'),
    # path('user-create/', views.UserOrderCreateView.as_view(), name='user_order_create')
]