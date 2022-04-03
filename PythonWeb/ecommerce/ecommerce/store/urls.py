from django.urls import path

from ecommerce.store.views import store, cart, checkout, update_item, wrong_input, order_completed, \
    checkout_emtpy_cart

urlpatterns = (
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout_empty_cart', checkout_emtpy_cart, name='checkout empty cart'),
    path('checkout/', checkout, name='checkout'),
    path('wrong_input/', wrong_input, name='wrong input'),
    path('order_completed/', order_completed, name='order completed'),


    path('update_item/', update_item, name='update item'),

)