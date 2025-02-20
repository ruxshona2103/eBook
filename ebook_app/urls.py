from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, ReviewViewSet, CategoryViewSet
from services.product_view_history import BookviewHistoryCreate
from services.flash_sale import FlashSaleListCreateView, check_flash_sale

router= DefaultRouter()
router.register(r'books', BookViewSet),
router.register(r'reviews', ReviewViewSet),
router.register(r'categories', CategoryViewSet),

urlpatterns = [
    path('', include(router.urls)),

    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),
    path('check-sale/<int:book_id>/', check_flash_sale, name='book-view-history-create'),
    path('book-view/', BookviewHistoryCreate.as_view(), name='book-view-history-create'),

]


