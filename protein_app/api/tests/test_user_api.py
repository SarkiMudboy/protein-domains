from .test_helpers import ResearcherTestHelper
from django.urls import reverse
from rest_framework import status

# urls

REGISTER = reverse('researchers:register')
RESEARCHERS = reverse('researchers:researcher')
LOGIN = reverse('researchers:login')


class ResearcherTestcase(ResearcherTestHelper):

    def reseaercher_can_create_account(self):

        user_data = self.user_data

        response = self.client.post(url=REGISTER, data=user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, 'User not created')

    def researcher_cannot_create_account_without_required_credentials(self):

        user_data = self.user_data
        user_data.pop('username')