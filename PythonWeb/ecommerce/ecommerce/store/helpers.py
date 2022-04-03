import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from .models import *


# accepts a cookie name and an url, deletes the cookie and redirects to the url
def delete_cookie(cookie_name, redirect_to_str_url):
    response = redirect(redirect_to_str_url)
    response.delete_cookie(cookie_name)
    return response


def cookie_cart(request):
    try:
        cart_info = json.loads(request.COOKIES['cart'])
    except KeyError:
        cart_info = {}
    print("CART:", cart_info)
    items = []
    order = {'cart_total_sum': 0, 'cart_total_items_count': 0}

    for i in cart_info:

        # if a product present in the cookie cart has been deleted from the database by any reason skips it
        try:
            product = Product.objects.get(id=i)
        except ObjectDoesNotExist:
            continue

        quantity = cart_info[i]['quantity']
        total = (product.price * quantity)

        order['cart_total_sum'] += total
        order['cart_total_items_count'] += quantity

        order_item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'image': product.image,
                'in_stock': product.in_stock,
            },
            'quantity': quantity,
            'total_price': total
        }
        items.append(order_item)
    return {'order': order, 'items': items}
