from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Coffee



# Create your views here.
def home(request):
    coffee =Coffee.objects.all()
    return render(request,'home.html',{'coffee':coffee})

def start(request):
    return render(request,'index.html')


