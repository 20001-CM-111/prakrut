from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('CreateAccount/',views.CreateAccount,name='CreateAccount'),
    path('',views.Login,name='Login'),
    path('Home/',views.Home,name='Home'),
    path('FarmerForm/', views.Form, name='Form'),
    path('Price/',views.Price,name='Price'),
    path('reset_password/',v.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',v.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',v.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',v.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
