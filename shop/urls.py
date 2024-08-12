from django.urls import path

from shop import views

app_name = 'shop'
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path(
        'products/<slug>/',
        views.ProductDetailView.as_view(),
        name='product-detail'
    ),
]
