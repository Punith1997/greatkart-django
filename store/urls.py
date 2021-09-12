from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    re_path('search/', views.search, name='search'),
]
