from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>/', views.product, name='product'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register' ),
    path('wishlist/', views.wishlist, name='wishlist'),
]

