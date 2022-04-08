from django.urls import path

from ecommerce.registration.views import register, registration_completed, email_already_in_use, UserLoginView, \
    UserLogoutView

urlpatterns = (
    path('', register, name='register'),
    path('registration_completed/', registration_completed, name='registration completed'),
    path('email_already_in_use/', email_already_in_use, name='email already in use'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
)

