# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
from django.shortcuts import render
from person.models import Person
import json
# Create your views here.

def index(request):
    return render(request, 'index.html')
def data(request):
    form_data = request.POST
    name = form_data.get('name')
    age = form_data.get('age')
    birth = form_data.get('birth')
    Person.objects.create(name=name, age=age, birth=birth)
    response_data = {
        'name': name,
        'age': age,
        'birth': birth
    }
    return HttpResponse(json.dumps(response_data))

def emit(request):
    form_data = request.POST
    print(form_data)
    name = form_data.get('name')
    age = form_data.get('age')
    birth = form_data.get('birth')
    Person.objects.create(name=name, age=age, birth=birth)
    response_data = {
        'name': name,
        'age': age,
        'birth': birth
    }
    return render(request, 'show.html', locals())