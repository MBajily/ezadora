from django.urls import path
from . import views

urlpatterns = [
	path('collection/', views.collection, name="collection"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
]