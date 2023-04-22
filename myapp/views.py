from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *




def index(request):
    data = student.objects.all()
 
    return render(request, 'index.html', {"data": data})

