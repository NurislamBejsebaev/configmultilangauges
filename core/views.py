from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


    def get_queryset(self):
        # Передайте параметры фильтрации, если они есть
        queryset = BookFilter(self.request.GET, queryset=super().get_queryset(), request=self.request).qs
        return queryset

