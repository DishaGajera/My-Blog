from .forms import StyledLoginForm
from django.contrib.auth import views as auth_views
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html',
        authentication_form=StyledLoginForm
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('createpost/', views.create_post, name='create_post'),

]