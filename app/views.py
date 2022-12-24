from django.shortcuts import render
from .models import *

def home_page(request):
    return render(request, 'app/home_page.html')

def app_list(request):
    products = Product.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'products': products,
        'rubrics': rubrics
    }
    return render(request, 'app/app_list.html', context)

def app_detail(request, rubric_id):
    products = Product.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'products': products,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    return render(request, 'app/app_detail.html', context)


