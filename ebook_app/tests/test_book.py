from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ebook_app.models import Book, Category, Review, User
from django.contrib.auth import get_user_model

User = get_user_model()

class BookViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="ruxshona", password='1111')
        self.staff_user=User.objects.create_user(username="rayxona", password='rayxona', is_staff=True)


        self.category1= Category.objects.create(name='Jahon adabiyoti')
        self.category2= Category.objects.create(name='Detektiv asarlar')

        self.book1 = Book.objects.create(name="Jarayon", description="Franz Kafkaning mashhur araslaridan biri", category=self.category1, price=65000)
        self.book2 = Book.objects.create(name="Izquvar Puaro", description="Agata Kristining bestseller asarlaridan", category=self.category2, price=48000)

        Review.objects.create(book=self.book1, rating=5, user_id = 1)
        Review.objects.create(book=self.book1, rating=3, user_id = 2)
        Review.objects.create(book=self.book2, rating=4, user_id = 1)

    def test_book_list(self):
        url = reverse('book-list')
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']),  2)

    def test_top_rated(self):
        url = reverse('book-top-rated')
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Jarayon')

    def test_average_rating(self):
        url = reverse('book-average-rating', args=[self.book1.id])
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['average_rating'], 4)

    def test_permission_denied_for_anonymous_create(self):
        self.client.force_authenticate(user=None)
        url = reverse('book-list')
        data={'name': 'Brother', 'description':'Triller kitob', 'price':66000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
