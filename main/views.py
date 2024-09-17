from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm

def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'npm' : '2306275102',
        'name': 'Abraham Jordy Ollen',
        'class': 'PBP C',
        'product_entries': product_entries,
    }

    return render(request, "main.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_product(request):
        form = ProductForm(request.POST or None)
        if form.is_valid() and request.method == "POST":
             form.save()
             return redirect('main:show_main')
        context = {'form' : form}
        return render(request, "create_product.html", context)
