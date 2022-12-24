from django.shortcuts import render
from .models import *

def home_page(request):
    authors = Authors.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'app/home_page.html', context)

