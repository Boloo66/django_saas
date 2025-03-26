from django.shortcuts import render
from . import views

def home_page_view(request, *args, **kwargs):
    return render(request, 'home.html') 