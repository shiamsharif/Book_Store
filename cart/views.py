from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from Product.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    # Since quantity is always 1, we don't need to process the form data
    cart.add(product=product)
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    # Since quantity is always 1, we can simplify this
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})