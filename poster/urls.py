from django.urls import path
from .views import post_list, register, create_post
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', post_list, name='post_list'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', create_post, name='create_post'),
]