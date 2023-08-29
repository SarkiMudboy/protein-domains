from django.test import TestCase
from rest_framework.test import APIClient
import factory
from ..factory import DomainFactory, PfamFactory
from users.factory import UserFactory
from abstract.tests.test_helpers import TestHelper
from .api_test_fixtures import APIData

class DomainTestHelper(TestHelper):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.user = UserFactory.create()
        cls.pfam = PfamFactory.create()
        cls.domain = DomainFactory.create()
        cls.api_data = APIData()
        cls.client = APIClient()

    def tearDown(self) -> None:
        return super().tearDown()
    
