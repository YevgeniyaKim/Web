from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.products),
    path('products/<int:product_id>/', views.product),
    path('categories/', views.categories),
    path('categories/<int:category_id>/', views.category),
    path('categories/<int:category_id>/products', views.category_products),
]