from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('add_estimate', views.add_estimate)
]