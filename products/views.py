from django.shortcuts import render, get_object_or_404
from .models import Product

from .forms import ProductForm


def products(request):
    """
    A view to return all products in our store.
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to return the individual product information.
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)



def add_product(request):
    """ Add a new product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
