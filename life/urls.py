from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/',views.index, name='posts'),
    path('answers/',views.index, name='answers')
]