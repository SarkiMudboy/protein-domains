from protein.factory import ProteinFactory, TaxaFactory
from domain.factory import DomainFactory
from domain.models import Domain
from rest_framework.test import APIClient
import factory
from protein.models import Protein, Taxa
from users.factory import UserFactory
from abstract.tests.test_helpers import TestHelper
from .protein_fixtures import APIData
from django.urls import reverse
from typing import Any


class ProteinTestHelper(TestHelper):

    @classmethod
    def setUpTestData(cls):
        
        cls.user = UserFactory.create()
        cls.proteins = factory.create_batch(Protein, 10, FACTORY_CLASS=ProteinFactory)
        cls.taxa = factory.create_batch(Taxa, 10, FACTORY_CLASS=TaxaFactory)
        cls.client = APIClient()
        cls.data = APIData()

    def tearDown(self) -> None:
        return super().tearDown()
    
    def build_url(self, endpoint: str, **kwargs: Any) -> str:
        return reverse(endpoint, kwargs=kwargs)
    
    def create_protein_with_domains(self):

        domains = factory.create_batch(Domain, 10, FACTORY_CLASS=DomainFactory)
        return ProteinFactory.create(domains=domains)