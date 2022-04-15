from django.urls import path

from ecommerce.registration.views import register, registration_completed, email_already_in_use, UserLoginView, \
    UserLogoutView, terms, ChangeUserPasswordView, ResetUserPasswordView, ResetUserPasswordDoneView, \
    ResetUserPasswordConfirmView, ResetUserPasswordCompleteView,  delete

urlpatterns = (
    path('', register, name='register'),
    path('registration_completed/', registration_completed, name='registration completed'),
    path('email_already_in_use/', email_already_in_use, name='email already in use'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('terms/', terms, name='terms'),
    path('change_password/', ChangeUserPasswordView.as_view(), name='change password'),

    path('reset_password/', ResetUserPasswordView.as_view(), name='reset_password'),
    path('reset_password_sent/', ResetUserPasswordDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetUserPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', ResetUserPasswordCompleteView.as_view(), name='password_reset_complete'),
    path('delete_user/', delete, name='delete user'),
)

