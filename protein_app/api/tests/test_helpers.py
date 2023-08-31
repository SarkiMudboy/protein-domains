from rest_framework.test import APIClient
import factory
from users.factory import UserFactory
from abstract.tests.test_helpers import TestHelper
from django.urls import reverse
from rest_framework.authtoken.models import Token

class ResearcherTestHelper(TestHelper):
    
    @classmethod
    def setUpTestData(self):

        self.user = UserFactory.create()
        self.client = APIClient()
        self.user_data = factory.build(dict, FACTORY_CLASS=UserFactory)

        self.user_data['password2'] = self.user_data.get('password')

        self.test_password = 'its-a-secret'

        self.user_auth_token = Token.objects.get(user=self.user)

    def tearDown(self) -> None:
        return super().tearDown()
    

    def build_url(self, endpoint, **kwargs):

        return reverse(endpoint, kwargs=kwargs)
