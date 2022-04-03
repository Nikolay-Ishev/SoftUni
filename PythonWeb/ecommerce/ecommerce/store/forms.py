from django import forms

from ecommerce.store.models import Customer, ShippingAddress


# adds the widget 'form-control' to every model form child
class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


class CreateCustomerForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone_number')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': "First name..",
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': "Last name..",
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': "Email..",
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'placeholder': 'Phone number..',
                }
            )
        }
        labels = {
            'first_name': "",
            'last_name': "",
            'email': "",
            'phone_number': "",
        }


class CreateAddressForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = ShippingAddress
        fields = ('city', 'zipcode', 'address')
        widgets = {
            'city': forms.TextInput(
                attrs={
                    'placeholder': "City..",
                }
            ),
            'zipcode': forms.NumberInput(
                attrs={
                    'placeholder': "Zipcode..",
                    'min': 0,
                    'max': 9999,
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': "Address..",
                }
            ),
        }

        labels = {
            'address': "",
            'city': "",
            'zipcode': "",
        }
