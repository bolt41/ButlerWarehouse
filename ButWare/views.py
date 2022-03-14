from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .forms import *
from .forms import *
from .models import *


@login_required
def index(request):
    return render(request, 'main.html', {})


@login_required
def add_estimate(request):
    if request.POST:
        print (request.POST)
    form = AddEstimate()
    data_tovar = Product.objects.all()
    context = {
        'form': form,
        'title': 'Добавление сметы',
        'data_tovar': data_tovar
    }
    return render(request, 'estimate/add_estimate.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')