from rest_framework import serializers
from .models import Book
from django.utils.translation import gettext_lazy as _


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = _('__all__')
