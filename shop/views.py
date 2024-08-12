from django.views import generic

from shop.models import Product, ProductCategory


class ProductCategoryContextMixin(generic.base.ContextMixin):
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = ProductCategory.objects.all()
        return data


class ProductListView(ProductCategoryContextMixin, generic.ListView):
    model = Product
    paginate_by = 10


class ProductDetailView(ProductCategoryContextMixin, generic.DetailView):
    model = Product
