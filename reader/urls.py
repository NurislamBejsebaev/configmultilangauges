from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReaderViewSet, BookReadeingViewSet

router = DefaultRouter()
router.register(r'readers', ReaderViewSet)
router.register(r'bookreading', BookReadeingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
]