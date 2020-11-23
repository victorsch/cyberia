from django.urls import path

from . import views

urlpatterns = [
    path('', views.newsportal, name='index'),
    path('/news', views.newsportal, name='newsportal'),
]
