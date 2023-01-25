from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category

class UpTest(APITestCase):
    def test_create_list(self):
        response = self.client.get('reverse/')
        print(response)

