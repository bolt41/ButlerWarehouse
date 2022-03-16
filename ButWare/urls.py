from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('estimate_json/', views.Estimate_asJson, name='estimate_json'),
    path('add_estimate', views.add_estimate, name='add_estimate'),
    path('autocomplete', views.autocomplete, name='autocomplete'),
    path('smeta', views.smeta, name='smeta'),
]