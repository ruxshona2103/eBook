from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, ReviewViewSet, CategoryViewSet, OrderViewSet
from ebook_app.services.product_view_history import BookviewHistoryCreate
from ebook_app.services.flash_sale import FlashSaleListCreateView, check_flash_sale
from .services import admin_replenish_stock

router= DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),
    path('check-sale/<int:book_id>/', check_flash_sale, name='book-view-history-create'),
    path('book-view/', BookviewHistoryCreate.as_view(), name='book-view-history-create'),
    path('admin/replenish_stock/<int:book_id>/<int:amount>', admin_replenish_stock, name='admin_replenish_stock'),

]


