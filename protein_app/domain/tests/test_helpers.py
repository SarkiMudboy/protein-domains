from django.test import TestCase
from rest_framework import APIClient
import factory
from ..factory import Domainfactory, PfamFactory
from users.factory import UserFactory
from abstract.tests.test_helpers import TestHelper


class DomainTestHelper(TestHelper):

    def setUpTestData(self):

        self.user = UserFactory.create()
        self.pfam = PfamFactory.create()
        self.domain = Domainfactory.create()
        
        self.client = APIClient()

    def tearDown(self) -> None:
        return super().tearDown()
    
