from django.urls import path

from shop import views

app_name = 'shop'
urlpatterns = [
    path(
        'products/',
        views.ProductListView.as_view(),
        name='product-list',
    ),
    path(
        'products/<slug>/',
        views.ProductDetailView.as_view(),
        name='product-detail',
    ),
    path(
        'cart/',
        views.CartView.as_view(),
        name='cart',
    ),
    path(
        'products/<slug>/add-to-cart/',
        views.add_to_cart,
        name='add-to-cart',
    ),
    path(
        'products/<slug>/remove-from-cart/',
        views.remove_from_cart,
        name='remove-from-cart',
    ),
    path(
        'products/cart/empty/',
        views.empty_cart,
        name='empty-cart',
    ),
]
