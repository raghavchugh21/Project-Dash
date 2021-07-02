from carts.models import Cart, CartItem
from carts.views import _cart_id


def counter(request):
    if 'admin' in request.path:
        return {}
    else:
        try:
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart = Cart.objects.filter(cart_id=_cart_id(request))
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
            cart_count = 0
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            pass
    return dict(cart_count=cart_count)
