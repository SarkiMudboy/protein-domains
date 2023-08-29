from .test_helpers import DomainTestHelper
from django.urls import reverse
from rest_framework import status

# DOMAIN_URL = reverse('pfam:domain')
# GET_DOMAIN_URL = reverse('pfam:get-domain')
# UPDATE_DOMAIN_URL = reverse('pfam:update-domain')
# DELETE_DOMAIN_URL = reverse('pfam:delete-domain')

PFAM_URL = reverse('pfam:pfam-list')
# GET_DOMAIN_URL = reverse('pfam:get-domain')
# UPDATE_DOMAIN_URL = reverse('pfam:update-domain')
# DELETE_DOMAIN_URL = reverse('pfam:delete-domain')


class PfamTestCase(DomainTestHelper):

    def test_unauthorized_user_cannot_create_new_pfam(self):

        pfam_data = self.api_data.get_pfam_data()

        response = self.client.post(PFAM_URL, data=pfam_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorized_user_can_create_new_pfam(self):

        pfam_data = self.api_data.get_pfam_data()

        self.client.force_authenticate(user=self.user)

        response = self.client.post(PFAM_URL, data=pfam_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        


        
