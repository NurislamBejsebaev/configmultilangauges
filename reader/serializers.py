from rest_framework import serializers
from .models import Reader, BookReading


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'


class BookReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReading
        fields = '__all__'
