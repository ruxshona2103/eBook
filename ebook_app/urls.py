from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, ReviewViewSet, CategoryViewSet

router= DefaultRouter()
router.register(r'books', BookViewSet),
router.register(r'reviews', ReviewViewSet),
router.register(r'categories', CategoryViewSet),

urlpatterns = [
    path('', include(router.urls)),
]