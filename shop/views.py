from django.views import generic

from shop.models import Product, ProductCategory


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10

    def get_queryset(self):
        products = Product.objects.all()
        if 'category' in self.request.GET:
            products = products.filter(
                categories__slug=self.request.GET['category'],
            )
        return products

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['product_count'] = Product.objects.count()
        data['categories'] = ProductCategory.objects.all()
        data['category_slug'] = self.request.GET.get('category')
        return data


class ProductDetailView(generic.DetailView):
    model = Product
