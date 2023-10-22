from django_filters import rest_framework as filters
from .models import Book


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    genre = filters.CharFilter(field_name='genre', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'genre']
