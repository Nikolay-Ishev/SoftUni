from django.urls import path

from ecommerce.store.views import checkout, update_item, already_sold, order_completed, \
    checkout_emtpy_cart, Store, Cart, ProductDetails

urlpatterns = (
    path('', Store.as_view(), name='store'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout_empty_cart', checkout_emtpy_cart, name='checkout empty cart'),
    path('checkout/', checkout, name='checkout'),
    path('already_sold/', already_sold, name='already sold'),
    path('update_item/', update_item, name='update item'),
    path('order_completed/', order_completed, name='order completed'),
    path('details/<int:pk>/', ProductDetails.as_view(), name='details'),
)
