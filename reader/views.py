from rest_framework import viewsets
from .models import Reader, BookReading
from .serializers import ReaderSerializer, BookReadingSerializer
from rest_framework.permissions import IsAuthenticated


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = [IsAuthenticated]


class BookReadeingViewSet(viewsets.ModelViewSet):
    queryset = BookReading.objects.all()
    serializer_class = BookReadingSerializer
    permission_classes = [IsAuthenticated]
