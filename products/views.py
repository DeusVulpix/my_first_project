from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductsForm
from .models import Products


def products_list_view(request):
    queryset = Products.objects.all()
    context = {
        'products_list': queryset
    }
    return render(request, 'products/products_list.html', context)

def products_detail_view(request, id):
    obj = get_object_or_404(Products, id=id)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


def products_create_view(request):
    error = ''
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductsForm()
        else:
            error = 'Error 040'
    form = ProductsForm()
    context = {
        'form': form
    }
    return render(request,'products/products_create.html', context)


def products_upgrade_view(request, id):
    obj = get_object_or_404(Products, id=id)
    form = ProductsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request,'products/products_create.html', context)

def product_delete_view(request, id):
    obj = get_object_or_404(Products, id=id)
    if request.method == "POST":
        obj.delete()
        return render(request,'products/products_list.html')
    context = {
        "object": obj
    }
    return render(request, "products/products_delete.html", context)

