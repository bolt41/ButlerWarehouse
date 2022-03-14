from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('add_estimate', views.add_estimate, name='add_estimate'),
    path('autocomplete', views.autocomplete, name='autocomplete'),
    path('smeta', views.smeta, name='smeta'),
]