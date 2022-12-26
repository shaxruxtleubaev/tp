from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView
from .forms import ProductForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


def home_page(request):
    return render(request, 'app/home_page.html')


def app_list(request):
    products = Product.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'products': products,
        'rubrics': rubrics,
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

def manage(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'app/manage_list.html', context)

def ProductCreateView(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/manage/')
    context = {
        'form': form
    }
    return render(request, 'app/create.html', context)

def update(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/manage/')
    context = {
        'form': form
    }
    return render(request, 'app/update.html', context)

def delete(request, pk):
    product = Product.objects.filter(id=pk)
    product.delete()
    return redirect('/manage/')


def contact(request):
    return render(request, 'app/contact.html')
