from django.views import generic

from shop.models import Product, ProductCategory


class ProductCategoryContextMixin(generic.base.ContextMixin):
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = ProductCategory.objects.all()
        data['category_slug'] = self.request.GET.get('category')
        return data


class ProductListView(ProductCategoryContextMixin, generic.ListView):
    model = Product
    paginate_by = 10

    def get_queryset(self):
        if 'category' in self.request.GET:
            return Product.objects.filter(
                categories__slug=self.request.GET['category'],
            )
        else:
            return Product.objects.all()


class ProductDetailView(ProductCategoryContextMixin, generic.DetailView):
    model = Product
