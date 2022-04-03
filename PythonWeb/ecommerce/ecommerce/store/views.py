import datetime
import json

from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import CreateCustomerForm, CreateAddressForm
from .models import *
from .helpers import cookie_cart, delete_cookie


# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        cookie_data = cookie_cart(request)
        order = cookie_data['order']

    products = Product.objects.all()
    context = {
        'products': products,
        'order': order,
    }
    return render(request, 'store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        cookie_data = cookie_cart(request)
        order = cookie_data['order']
        items = cookie_data['items']
    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'cart.html', context)


def checkout(request):
    customer_form = CreateCustomerForm()
    address_form = CreateAddressForm()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

        # loop through order items and check if a product has already been sold before checking out
        for item in items:
            current_product = Product.objects.get(id=item.product_id)
            # removing the item if it has been sold
            if current_product.in_stock == 'Sold':
                item.delete()
        # refreshing the order items set
        items = order.orderitem_set.all()

        # creates an order if the request is POST
        if request.method == 'POST':
            if order.cart_total_items_count <= 0:
                return redirect('checkout empty cart')

            address, created = ShippingAddress.objects.get_or_create(customer=customer)
            customer_form = CreateCustomerForm(request.POST, instance=customer)
            address_form = CreateAddressForm(request.POST, instance=address)

            if address_form.is_valid() and customer_form.is_valid():
                transaction_id = datetime.datetime.now().timestamp()
                order.transaction_id = transaction_id
                order.complete = True
                address_form.save()
                customer_form.save()
                order.shipping_address = customer.shippingaddress
                order.save()
                return redirect('order completed')
            else:
                return redirect('wrong input')

        # visualise the user data in the form if the request is GET
        else:
            if hasattr(customer, 'shippingaddress'):
                address = ShippingAddress.objects.get(customer=customer)
                address_form = CreateAddressForm(instance=address)
            else:
                address_form = CreateAddressForm()
            customer_form = CreateCustomerForm(instance=customer)

    else:
        cookie_data = cookie_cart(request)
        order = cookie_data['order']
        items = cookie_data['items']

        # creates an order if the request is POST
        if request.method == 'POST':
            if not items:
                return redirect('checkout empty cart')

            customer_form = CreateCustomerForm(request.POST)
            address_form = CreateAddressForm(request.POST)
            print(customer_form.is_valid())
            print(address_form.is_valid())


            if address_form.is_valid() and customer_form.is_valid():

                customer, created = Customer.objects.update_or_create(
                    email=customer_form.cleaned_data.get("email"),
                    defaults={
                        'first_name': customer_form.cleaned_data.get("first_name"),
                        'last_name': customer_form.cleaned_data.get("last_name"),
                        'phone_number': customer_form.cleaned_data.get("phone_number"),
                    },

                )

                address, created = ShippingAddress.objects.update_or_create(
                    customer=customer,
                    defaults={
                        'city': address_form.cleaned_data.get("city"),
                        'zipcode': address_form.cleaned_data.get("zipcode"),
                        'address': address_form.cleaned_data.get("address"),
                    }
                )

                order = Order.objects.create(
                    customer=customer,
                    shipping_address=address,
                    complete=False
                )
                transaction_id = datetime.datetime.now().timestamp()
                order.transaction_id = transaction_id

                for item in items:
                    product = Product.objects.get(id=item['product']['id'])
                    order_item = OrderItem.objects.create(
                        product=product,
                        order=order,
                        quantity=item['quantity']
                    )
                    order_item.save()

                order.complete = True
                order.save()
                return delete_cookie('cart', 'order completed')

    context = {
        'address_form': address_form,
        'customer_form': customer_form,
        'items': items,
        'order': order,
    }
    return render(request, 'checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add' and product.in_stock != 'Sold':
        if product.in_stock == 'Unique':
            order_item.quantity = 1
        else:
            order_item.quantity += 1
        order_item.save()

    elif action == 'remove':
        if order_item.quantity > 1:
            order_item.quantity -= 1
            order_item.save()
        else:
            order_item.delete()

    return JsonResponse('Item was added', safe=False)


def wrong_input(request):
    return render(request, 'wrong_input.html')


def order_completed(request):
    return render(request, 'order_completed.html')


def checkout_emtpy_cart(request):
    return render(request, "checkout_empty_cart.html")
