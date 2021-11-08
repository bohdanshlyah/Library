"""djangoViewTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, handler403, handler404


from .views import index, permission_denied_view, page_not_found_view

urlpatterns = [
    path('', index, name='index'),
    # path('403/', permission_denied_view),
    path('404/', page_not_found_view),
    path('auth/', include('authentication.urls')),
    path('order/', include('order.urls')),
    path('book/', include('book.urls')),
    path('author/', include('author.urls')),
    path('admin/', admin.site.urls),
]

handler403 = 'library.views.permission_denied_view'
handler404 = 'library.views.page_not_found_view'