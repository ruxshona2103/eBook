from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework import generics, serializers, status
from rest_framework.pagination import PageNumberPagination

from django_filters import rest_framework as django_filters


from ebook_app.models import Book,  FlashSale, BookViewHistory
from ebook_app.filters import FlashSaleFilter

class CustomPagination(PageNumberPagination):
    page_size = 3


class FlashSaleListCreateView(generics.ListCreateAPIView):
    queryset = FlashSale.objects.all()

    class FlashSaleSerializer(serializers.ModelSerializer):

        class Meta:
            model = FlashSale
            fields = ('id','book', 'discount_percentage', 'start_time', 'end_time')


    serializer_class = FlashSaleSerializer
    pagination_class = CustomPagination

    filter_backends = (django_filters.DjangoFilterBackend)
    filterset_class = FlashSaleFilter


@api_view(['GET'])
def check_flash_sale(request, book_id):
    try:
        book = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return Response({"error": "THis kind of book  not fount."}, status=status.HTTP_404_NOT_FOUND)

    user_viewed = BookViewHistory.objects.filter(user=request.user, book=book).exists()

    upcoming_flash_sale = FlashSale.objects.filter(
        book = book,
        start_time__lte = datetime.now() + timedelta(hours=24)
    ).first()

    if user_viewed and upcoming_flash_sale:
        discount = upcoming_flash_sale.discount_percentage
        start_time = upcoming_flash_sale.start_time
        end_time = upcoming_flash_sale.end_time
        return Response(
            {
                "message": f"This book will be on a {discount}% off flash sale !",
                "start_time": start_time,
                "end_time": end_time
             }
        )
    else:
        return Response({
            "message": "No upcoming flash sale for this book."
        })






