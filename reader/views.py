from rest_framework import viewsets
from .models import Reader, BookReading
from .serializers import ReaderSerializer, BookReadingSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class BookReadeingViewSet(viewsets.ModelViewSet):
    queryset = BookReading.objects.all()
    serializer_class = BookReadingSerializer
