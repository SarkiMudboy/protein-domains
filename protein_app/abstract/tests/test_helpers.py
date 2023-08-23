from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
import factory
from users.factory import UserFactory

class TestHelper(APITestCase):

    def setUpTestData(self):

        return super().setUpTestData()

    def tearDown(self) -> None:

        return super().tearDown()
    
        
