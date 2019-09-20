from django.test import TestCase

from api import models
from .mock_data import category_data, favorite_data

import json

class TestModels(TestCase):

    def setUp(self):
        category = models.Category.objects.create(**category_data)
        favorite_data['category'] = category
        self.favorite = models.Favorite.objects.create(**favorite_data)

    def test_favorite(self):
        title = favorite_data.get('title')
        ranking = category_data.get('ranking')
        obj = models.Favorite.objects.get(title=title)
        self.assertEqual(obj.title, title)
        self.assertEqual(obj.category.ranking, ranking)

    def test_category(self):
        ranking = category_data.get('ranking')
        category_name = category_data.get('category_name')
        obj = models.Category.objects.get(
                ranking=ranking,
                category_name=category_name
            )
        self.assertEqual(obj.ranking, ranking)
        self.assertEqual(obj.category_name, category_name)

    def test_auditlog(self):
        ranking = category_data.get('ranking')
        category_name = category_data.get('category_name')
        title = favorite_data.get('title')
        obj = models.Category.objects.get(
                ranking=ranking,
                category_name=category_name
            )
        auditlog = models.Auditlog.objects.filter(
                        favorite=self.favorite.id
                    )
        content = json.loads(auditlog[0].content)
        self.assertEqual(content.get('title'), title)
