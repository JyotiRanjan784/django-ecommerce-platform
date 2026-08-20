from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    #path("", views.about, name="ShopHome"),
    path('', views.index, name='index'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='Search'),
    path('products/<int:myid>/', views.productView, name='productView'),
    path('checkout/', views.checkout, name='Checkout'),
    path('payment/', views.payment, name='payment'),
    path('payment-success/', views.payment_success, name='payment_success')
]