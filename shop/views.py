from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
)
from django.views import generic

from shop.models import Product, ProductCategory


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10

    def get_queryset(self):
        if 'search' in self.request.GET and self.request.GET['search'] != '':
            vector = (
                SearchVector('name', weight='A')
                + SearchVector('category_names', weight='A')
                + SearchVector('description', weight='D')
            )
            query = SearchQuery(self.request.GET['search'])
            products = Product.objects.annotate(
                category_names=ArrayAgg('categories__name', distinct=True),
                rank=SearchRank(vector, query),
            ).filter(rank__gte=0.1).order_by('-rank')
        else:
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
