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


class ProductCreateView(CreateView):
    template_name = 'app/create.html'
    form_class = ProductForm
    success_url = reverse_lazy('app_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def manage(request):
    products = Product.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'products': products,
        'rubrics': rubrics
    }
    return render(request, 'app/manage_list.html', context)


'''
def update(request, pk):
    app = Product.objects.get(id=pk)
    form = ProductForm(instance=app)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=app, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/app_list/manage/')
    context = {
        'form': form
    }
    return render(request, 'update.html', context)

def delete(request, pk):
    app = Product.objects.get(id=pk)
    app.delete()
    return redirect('/app_list/')
'''
