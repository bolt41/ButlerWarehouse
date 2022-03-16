from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

#функция выдачи автозаполнения товаров из БД
def autocomplete(request):
    if 'term' in request.GET:
        qs = Product.objects.filter(name__istartswith=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.name)
        return JsonResponse(titles, safe=False)


def Estimate_asJson(request):
    object_list = Estimate.objects.all() #or any kind of queryset
    data = [object.get_estimate_json() for object in object_list]
    response = {'data': data}
    print(response)
    return JsonResponse(response)


@login_required
def index(request):
    return render(request, 'main.html', {})


@login_required
def add_estimate(request):
    if request.POST:
        print (request.POST)
    else:

        person = serializers.serialize("json", ObjectsCurrent.objects.all(), fields="name")
        print(type(person))
        data = {"data": person}
        print(person)
        return render(request, 'estimate/add_estimate.html', context=data)

@login_required
def smeta(request):
    all_estimate = Estimate.objects.all()
    context = {
        'estimate': all_estimate,
    }
    return render(request, 'estimate/smeta.html', context=context)

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')