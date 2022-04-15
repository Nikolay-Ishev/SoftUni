from django.core.exceptions import ValidationError
from django.test import TestCase

from ecommerce.store.models import Customer


class CustomerTests(TestCase):
    VALID_CUSTOMER_DATA = {
        "first_name": 'Nikolay',
        "last_name": 'Ishev',
        "phone_number": "+359 896 66 97 68",
        "email": 'n.test@gmail.com',
    }

    def test_customer_create__when_phone_number_contains_numbers_only__expect_success(self):
        self.VALID_CUSTOMER_DATA["phone_number"] = "0888919293"
        customer = Customer(**self.VALID_CUSTOMER_DATA)
        customer.save()

    def test_customer_create__when_phone_number_contains_numbers_and_spaces__expect_success(self):
        self.VALID_CUSTOMER_DATA["phone_number"] = "0888 919 293"
        customer = Customer(**self.VALID_CUSTOMER_DATA)
        customer.save()

    def test_customer_create__when_phone_number_contains_numbers_spaces_and_a_plus_sign__expect_success(self):
        customer = Customer(**self.VALID_CUSTOMER_DATA)
        customer.save()

    def test_customer_create__when_phone_number_contains_a_dollar_sign__expect_to_fail(self):
        self.VALID_CUSTOMER_DATA["phone_number"] = "$0888919293"
        customer = Customer(**self.VALID_CUSTOMER_DATA)
        with self.assertRaises(ValidationError) as context:
            customer.full_clean()
            customer.save()
        self.assertIsNotNone(context.exception)

    def test_customer_create__when_phone_number_contains_an_underscore__expect_to_fail(self):
        self.VALID_CUSTOMER_DATA["phone_number"] = "0888_919293"
        customer = Customer(**self.VALID_CUSTOMER_DATA)
        with self.assertRaises(ValidationError) as context:
            customer.full_clean()
            customer.save()
        self.assertIsNotNone(context.exception)

    def test_customer_create__when_phone_number_contains_a_letter__expect_to_fail(self):
        self.VALID_CUSTOMER_DATA["phone_number"] = "0888919293phone"
        customer = Customer(**self.VALID_CUSTOMER_DATA)
        with self.assertRaises(ValidationError) as context:
            customer.full_clean()
            customer.save()
        self.assertIsNotNone(context.exception)

    def test_customer_create__when_vaid__expect_correct_str_method(self):
        customer = Customer(**self.VALID_CUSTOMER_DATA)
        expected_full_name = f'{self.VALID_CUSTOMER_DATA["first_name"]} {self.VALID_CUSTOMER_DATA["last_name"]}'
        self.assertEqual(expected_full_name, str(customer))
