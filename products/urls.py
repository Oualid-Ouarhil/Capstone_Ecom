from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.get_products,name='products'),
    path('products/<str:pk>/', views.get_id_product,name='get_id_product'),
    path('products/new', views.new_product,name='new_products'),
]