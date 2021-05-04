from django.shortcuts import render
from django.http import HttpResponse
from .models import Answer
from django.template import loader

def home(request):
    template = loader.get_template('playground/home.html')
    return HttpResponse(template.render({}, request))
    
