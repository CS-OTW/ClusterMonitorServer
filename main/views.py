from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "main/main.html")
