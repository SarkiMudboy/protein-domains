from domain.models import Pfam, Domain
from rest_framework.test import APIClient
import factory
from ..factory import DomainFactory, PfamFactory
from users.factory import UserFactory
from abstract.tests.test_helpers import TestHelper
from .api_test_fixtures import APIData
from django.urls import reverse


class DomainTestHelper(TestHelper):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.user = UserFactory.create()
        cls.pfams = factory.create_batch(Pfam, 10, FACTORY_CLASS=PfamFactory)
        cls.domains = factory.create_batch(Domain, 10, FACTORY_CLASS=DomainFactory)
        cls.api_data = APIData()
        cls.client = APIClient()

    def tearDown(self) -> None:
        return super().tearDown()
    
    def build_url(self, endpoint, **kwargs):

        return reverse(endpoint, kwargs=kwargs)
    
    def get_tokens(self):

        user = self.user

        endpoint = reverse('researcher:token_obtain_pair')

        response = self.client.post(endpoint, data={'username': user.get('username'), 
                                                    'password': UserFactory.raw_password()})
        
        self.tokens = response.json()
    
