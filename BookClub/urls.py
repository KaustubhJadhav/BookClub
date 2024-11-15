"""
URL configuration for BookClub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from BookClubApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubs/', views.club_list, name='club_list'),
    path('clubs/create/', views.club_create, name='club_create'),
    path('clubs/<int:pk>/edit/', views.club_update, name='club_update'),
    path('clubs/<int:pk>/delete/', views.club_delete, name='club_delete'),

    # Book URLs
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('', views.home, name='home'),
]
