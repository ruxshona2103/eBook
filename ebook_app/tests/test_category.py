from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ebook_app.models import Category
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class CategoryTests(APITestCase):
    fixtures = ['categories']

    def setUp(self):
       self.user = User.objects.create_user(username="Bexruz", password="bexruz")
       self.client.force_authenticate(user=self.user)
       self.category1 = Category.objects.first()


    def test_category_list(self):
        url = reverse('category-list')
        response= self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_category_create(self):
        url = reverse('category-list')
        data = {"name":"books"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category_update(self):
        url = reverse('category-detail', args=[self.category1.pk])
        data = {'name': "Bolalar kitoblari"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_delete(self):
        url = reverse('category-detail', args=[self.category1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


