from django.test import TestCase
from rest_framework import APIClient
import factory
from users.factory import UserFactory
from abstract.tests.test_helpers import TestHelper

class ProteinTestHelper(TestHelper):

    def setUpTestData(self):
        return super().setUpTestData()

    def tearDown(self) -> None:
        return super().tearDown()