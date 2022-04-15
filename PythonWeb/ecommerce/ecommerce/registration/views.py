from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from ecommerce.store.forms import CreateCustomerForm
from ecommerce.store.models import Customer


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('store')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('store')


'''
1 - Submit email form - PasswordResetView
2 - Email sent success message - PasswordResetDoneView
3 - Link to password reset from email - PasswordResetConfirmView
4 - Password successfully changed message - PasswordResetCompleteView

'''


class ResetUserPasswordView(PasswordResetView):
    template_name = 'reset_password.html'


class ResetUserPasswordDoneView(PasswordResetDoneView):
    template_name = 'reset_password_email_sent.html'


class ResetUserPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password_confirm.html'


class ResetUserPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'reset_password_done.html'


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy("registration completed")


def registration_completed(request):
    return render(request, 'registration_completed.html')


def email_already_in_use(request):
    return render(request, "email_already_in_use.html")


def register(request):
    if request.method == "POST":

        # check if a customer with the provided email already exists in the database before creating a form
        try:
            customer = Customer.objects.get(email=request.POST['email'])
            # if there is no account associated with the customer proceed with the registration
            if customer.user is None:
                customer_form = CreateCustomerForm(request.POST, instance=customer)
            else:
                return redirect('email already in use')
        except ObjectDoesNotExist:
            customer_form = CreateCustomerForm(request.POST)

        user_form = UserCreationForm(request.POST)

        if customer_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            user.email = customer.email
            user.save()
            login(request, user)
            return redirect('registration completed')
        else:
            return redirect('wrong input')

    else:
        customer_form = CreateCustomerForm()
        user_form = UserCreationForm()

    context = {
        'user_form': user_form,
        'customer_form': customer_form,
    }

    return render(request, 'register.html', context)


def terms(request):
    return render(request, 'terms.html')


def delete(request):
    request.user.delete()
    logout(request)
    return redirect('store')
