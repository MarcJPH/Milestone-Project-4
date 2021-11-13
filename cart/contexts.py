

def cart_contents(request):
    """
    Any items added to the cart will be available to all templates and apps
    """


    cart_items = []
    total = 0
    product_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,   
    }

    return context
