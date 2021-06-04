from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
        'products_count': products.count(),
    }
    return render(request, 'store/store.html', context)