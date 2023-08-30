from rest_framework.test import APIClient
import factory
from users.factory import UserFactory
from abstract.tests.test_helpers import TestHelper


class ResearcherTestHelper(TestHelper):
    
    @classmethod
    def setUpTestData(self):

        self.user = UserFactory.create()
        self.client = APIClient()
        self.user_data = factory.build(dict, FACTORY_CLASS=UserFactory)

        self.user_data['password2'] = self.user_data.get('password')

    def tearDown(self) -> None:
        return super().tearDown()
