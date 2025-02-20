from django_filters import rest_framework as django_filters
from .models import Book, FlashSale


class BookFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte'),
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte'),
    author_filter = django_filters.CharFilter(field_name='author', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['category','author']


class FlashSaleFilter(django_filters.FilterSet):
    min_percentage = django_filters.NumberFilter(field_name='discount_percentage', lookup_expr='gte'),
    max_percentage = django_filters.NumberFilter(field_name='discount_percentage', lookup_expr='lte'),

    class Meta:
        model = FlashSale
        fields = ['book']
