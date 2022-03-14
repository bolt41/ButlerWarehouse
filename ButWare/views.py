from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required
def index(request):
    return render(request, 'main.html', {})


@login_required
def add_estimate(request):
    form = AddEstimate
    return render(request, 'estimate/add_estimate.html', {'form': form, 'Title': 'Добавление сметы'})