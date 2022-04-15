from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ecommerce.store.models import Product, Customer, Order, OrderItem


class StoreTests(TestCase):
    USER_DATA = {
        'username': 'test',
        'password': 'test1234'
    }

    PRODUCTS_TO_CREATE = (
        Product(id=1, name="testBag", price=2),
        Product(id=2, name="testBag2", price=5)
    )

    USER = User(id=1, username='test', password='test1234')

    CUSTOMER = (Customer(
        id=1,
        user_id=1,
        first_name="Test",
        last_name="Testov",
        phone_number="0888001122",
        email="test@gmail.com"
    ),)

    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('store'))
        self.assertTemplateUsed(response, 'store.html')

    def test_get__when_two_products_expect_context_to_contain_two_products(self):
        # Arrange
        Product.objects.bulk_create(self.PRODUCTS_TO_CREATE)
        # Act
        response = self.client.get(reverse('store'))
        products = response.context['products']
        # Assert
        self.assertEqual(len(products), 2)

    def test_get__when_logged_in__expect_order_to_be_user_order(self):
        # Arrange
        user = User.objects.create(id=1, username='test')
        user.set_password('test1234')
        user.save()
        Customer.objects.bulk_create(self.CUSTOMER)
        customer_order = Order.objects.create(customer_id=1)
        Product.objects.bulk_create(self.PRODUCTS_TO_CREATE)
        order_item1 = OrderItem.objects.create(order=customer_order, product_id=1)
        order_item2 = OrderItem.objects.create(order=customer_order, product_id=2)
        # Act
        logged_in = self.client.login(**self.USER_DATA)
        response = self.client.get(reverse('store'))
        # Assert
        self.assertEqual(customer_order, response.context['order'])
