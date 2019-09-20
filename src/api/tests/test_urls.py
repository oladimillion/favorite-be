from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from mixer.backend.django import mixer

from api import models
from .mock_data import category_data, favorite_data


class TestUrls(APITestCase):
    
    def setUp(self):
        super(TestUrls, self).setUp()
        self.list_url = reverse('favorites-list')
        self.detail_url = reverse('favorites-detail', args=(1,))
        self.auditlog_url = reverse('auditlog')
        self.category_url = reverse('categories')
        self.category = mixer.blend(models.Category) 
        self.data = {**category_data, **favorite_data}


    def test_create_favorite_with_data(self):
        """
        Create favorite endpoint test.
        """
        url = self.list_url
        self.data['category'] = self.category.id
        response = self.client.post(url, self.data, format='json')
        favorite = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Favorite.objects.count(), 1)
        self.assertEqual(models.Auditlog.objects.count(), 1)
        self.assertEqual(
                self.data.get('title'),
                favorite.get('title')
            )

    def test_create_favorite_with_no_data(self):
        """
        Create favorite endpoint test.
        """
        url = self.list_url
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_favorite_list(self):
        """
        Get favorite list endpoint test.
        """
        url = self.list_url
        favorite = mixer.blend(models.Favorite) 
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Favorite.objects.count(), 1)
        self.assertEqual(models.Auditlog.objects.count(), 1)
        self.assertEqual(
                favorite.title,
                response.data.get('results')[0].get('title')
            )

    def test_update_favorite(self):
        """
        Update favorite endpoint test.
        """
        mixer.blend(models.Favorite) 
        url = self.detail_url
        data = { 'title': 'title as changed' }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Favorite.objects.count(), 1)
        self.assertEqual(models.Auditlog.objects.count(), 2)
        self.assertEqual(
                data.get('title'),
                response.data.get('title')
            )

    def test_get_favorite(self):
        """
        Get favorite by id endpoint test.
        """
        favorite = mixer.blend(models.Favorite) 
        url = self.detail_url
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Favorite.objects.count(), 1)
        self.assertEqual(models.Auditlog.objects.count(), 1)
        self.assertEqual(
                favorite.title,
                response.data.get('title')
            )

    def test_auditlog_with_no_data(self):
        """
        Get auditlog endpoint test.
        """
        url = self.auditlog_url
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Auditlog.objects.count(), 0)
        self.assertEqual(models.Favorite.objects.count(), 0)


    def test_category(self):
        """
        Get category endpoint test.
        """
        mixer.blend(models.Category) 
        url = self.category_url
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Category.objects.count(), 2)
