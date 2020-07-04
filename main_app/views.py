from django.shortcuts import render
from .models import Brand
from .forms import PurchaseForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def brands_index(request):
    brands = Brand.objects.all()
    return render(request, 'brands/index.html', {'brands': brands})


def brands_detail(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    purchase_form = PurchaseForm()
    return render(request, 'brands/detail.html', {
        'brand': brand,
        'purchase_form': purchase_form
    })


class BrandCreate(CreateView):
    model = Brand
    fields = '__all__'


class BrandUpdate(UpdateView):
    model = Brand
    fields = ['country', 'description', 'founded']


class BrandDelete(DeleteView):
    model = Brand
    success_url = '/brands/'
