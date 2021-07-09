from django.shortcuts import render
from store.models import Product


def HomePage(request):
    if Product.objects.all().filter(is_available=True).exists():
        products = Product.objects.all().filter(is_available=True)
    else:
        products = None
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)