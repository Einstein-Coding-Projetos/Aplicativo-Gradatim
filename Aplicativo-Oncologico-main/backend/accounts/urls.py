from django.urls import path
from .views import AccountsRootView, ForgotPasswordView, MeView, RegisterView, ResetPasswordView

urlpatterns = [
    path('', AccountsRootView.as_view(), name='accounts-root'),
    path('me/', MeView.as_view(), name='me'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]
