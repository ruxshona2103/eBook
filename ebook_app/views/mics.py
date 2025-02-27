from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ebook_app.models import Order
from ebook_app.models import Review, Category
from ebook_app.permissions import IsOwnerReadOnly
from ebook_app.serializers import OrderSerializer
from ebook_app.serializers import ReviewSerializer, CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # default =  AllowAny

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
