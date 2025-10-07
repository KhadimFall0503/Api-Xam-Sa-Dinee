# api/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Rubrique

class TestRubriqueAPI(APITestCase):
    def setUp(self):
        self.rubrique = Rubrique.objects.create(title="Tech")

    def test_get_rubriques(self):
        response = self.client.get("/api/rubriques/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
