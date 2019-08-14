# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')
def data(request):
    form_data = request.POST
    name = form_data.get('name')
    age = form_data.get('age')
    birth = form_data.get('birth')
    print(name)
    print(age)
    print(birth)
    return HttpResponse('ok')
