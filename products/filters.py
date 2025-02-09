import django_filters

from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    search = django_filters.filters.CharFilter(field_name="name",lookup_expr="icontains")
    minimumprice = django_filters.filters.NumberFilter(field_name="price" or 0,lookup_expr="gte")
    maximumprice = django_filters.filters.NumberFilter(field_name="price" or 999999,lookup_expr="lte")  
    

    class Meta:
        model = Product
        fields = ['category', 'stock_quantity', 'search', 'minimumprice', 'maximumprice'] 