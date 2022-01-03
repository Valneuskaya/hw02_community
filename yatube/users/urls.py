from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [path('signup/',
               views.SignUp.as_view(),
               name='signup'),
               path('login/',
               LoginView.as_view(template_name='users/login.html'),
               name='login'),
               path('logout/',
               LogoutView.as_view(template_name='users/logged_out.html'),
               name='logout'),
               path('password_change_done/',
               PasswordResetView.as_view(
                    template_name='users/password_change_done.html'),
               name='password_change_done',),
               path('password_change_form/',
               PasswordResetView.as_view(
                    template_name='users/password_change_form.html'),
               name='password_change_form',),
               path('password_change_complete/',
               PasswordResetView.as_view(
                    template_name='users/password_change_complete.html'),
               name='password_change_complete'),
               path('password_change_confirm/',
               PasswordResetView.as_view(
                    template_name='users/password_change_confirm.html'),
               name='password_change_confirm',),
               path('password_reset_done/',
               PasswordResetView.as_view(
                    template_name='users/password_reset_done.html'),
               name='password_reset_done',),
               path('password_reset_form/',
               PasswordResetView.as_view(
                    template_name='users/password_reset_form.html'),
               name='password_reset_form',), ]
