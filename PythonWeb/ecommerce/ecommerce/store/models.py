from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, RegexValidator

# custom validators
phone_regex = RegexValidator(regex=r'^[0-9+\s]+$', message="Please enter a valid phone number.")


# Create your models here.
class Customer(models.Model):
    NAME_MAX_LENGTH = 30
    EMAIL_MAX_LENGTH = 120

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    phone_number = models.CharField(
        validators=(phone_regex,),
        max_length=22,
    )
    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    NAME_MAX_LENGTH = 120

    UNIQUE = 'Unique'
    MULTIPLE = 'Multiple'
    SOLD = 'Sold'
    IN_STOCK = [(x, x) for x in (UNIQUE, MULTIPLE, SOLD)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    in_stock = models.CharField(
        max_length=max(len(x) for x, _ in IN_STOCK),
        choices=IN_STOCK,
        default=UNIQUE
    )
    image = models.ImageField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class ShippingAddress(models.Model):
    ADDRESS_MAX_LENGTH = 240
    CITY_MAX_LENGTH = 120
    ZIPCODE_MAX_LENGTH = 4
    MAX_ZIPCODE = 9999

    customer = models.OneToOneField(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
    )
    address = models.CharField(
        max_length=ADDRESS_MAX_LENGTH,
    )
    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
    )
    zipcode = models.PositiveIntegerField(
        validators=(
            MaxValueValidator(MAX_ZIPCODE),
        ),
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.address


class Order(models.Model):
    TRANSACTION_ID_MAX_LENGTH = 120

    shipping_address = models.ForeignKey(
        ShippingAddress,
        on_delete=models.SET_NULL,
        null=True,
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
    )
    date_ordered = models.DateTimeField(
        auto_now_add=True,
    )
    complete = models.BooleanField(
        default=False,
    )
    transaction_id = models.CharField(
        max_length=TRANSACTION_ID_MAX_LENGTH,
        null=True,
    )

    @property
    def cart_total_sum(self):
        order_items = self.orderitem_set.all()
        total = sum([item.total_price for item in order_items])
        return total

    @property
    def cart_total_items_count(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    @property
    def cart_items_set(self):
        order_items = self.orderitem_set.all()
        return order_items

    def __str__(self):
        c = 'Completed' if self.complete else 'Not Completed'

        return f'Order number {self.id} with status "{c}"'


class OrderItem(models.Model):
    DEFAULT_QUANTITY = 0

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(
        default=DEFAULT_QUANTITY,
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    @property
    def total_price(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return self.product.name
