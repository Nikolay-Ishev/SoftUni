from django.test import TestCase
from ecommerce.store.forms import CreateCustomerForm


class CreateCustomerFormTests(TestCase):

    VALID_CUSTOMER_DATA = {
        "first_name": 'Nikolay',
        "last_name": 'Ishev',
        "phone_number": "+359 896 66 97 68",
        "email": 'n.test@gmail.com',
    }

    def test_CreateCustomerForm_validData(self):
        form = CreateCustomerForm(self.VALID_CUSTOMER_DATA)
        self.assertTrue(form.is_valid())


