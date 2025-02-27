from django.http import JsonResponse,HttpResponseBadRequest
from django.contrib.admin.views.decorators import staff_member_required
from ebook_app.models import Book
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

@api_view(['POST'])
@swagger_auto_schema(operation_description="Admin replenish stock for product")
@staff_member_required
def admin_replenish_stock(request, book_id, amount):
    try:
        # amount = int(request.POST.get('amount', 0))
        book = Book.objects.get(id=book_id)
        book.increase_stock(amount)

        return JsonResponse({'status': 'success', 'message': f'Successfully replenished stock by {amount}'})

    except Book.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product does not exist'}, status=400)

    except ValueError:
        return HttpResponseBadRequest('Invalid input.')


