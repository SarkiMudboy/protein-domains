from .test_helpers import DomainTestHelper
from django.urls import reverse
from rest_framework import status
from domain.models import Pfam, Domain


PFAM_URL = reverse('pfam:pfam-list')
GET_PFAM = 'pfam:get-pfam-domain'
PFAM_GET_TAXA_URL = 'pfam:get-pfam-taxa'
PFAM_UPDATE = 'pfam:pfam-update'
PFAM_DELETE = 'pfam:pfam-delete'

OBTAIN_TOKEN_PAIR = reverse('researchers:token_obtain_pair')
REFRESH_TOKEN = reverse('researchers:token_refresh')

GET_DOMAIN_URL = 'pfam:get-domain'
UPDATE_DOMAIN_URL = 'pfam:update-domain'
DELETE_DOMAIN_URL = 'pfam:delete-domain'


class PfamTestCase(DomainTestHelper):

    def test_unauthenticated_user_cannot_create_new_pfam(self):

        pfam_data = self.api_data.get_pfam_data()

        response = self.client.post(PFAM_URL, data=pfam_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        with self.assertRaises(Pfam.DoesNotExist):
            Pfam.objects.get(domain_id=pfam_data.get('domain_id'))

    def test_authenticated_user_can_create_new_pfam(self):

        pfam_data = self.api_data.get_pfam_data()

        # temporary: replace later

        pfam_data['domain_id'] = "PF10101099"

        self.client.force_authenticate(user=self.user)

        response = self.client.post(PFAM_URL, data=pfam_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # self.assertIn()

    def anon_user_cannot_perform_mod_operations(self):

        pfam = self.pfams[0]

        # UPDATE

        update_data = {'domain_id': 'PF033423', 'description': 'updated description'}

        endpoint = self.build_url(PFAM_UPDATE, kwargs={'pk': pfam.pk})

        response = self.client.post(endpoint, data=update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # DELETE

        endpoint = self.build_url(PFAM_DELETE, kwargs={'pk': pfam.pk})

        response = self.client.post(endpoint, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def anon_user_can_perform_read_operations(self):

        pfam = self.pfams[0]

        endpoint = self.build_url(GET_PFAM, kwargs={'domain_id': pfam.pk})

        response = self.client.get(GET_PFAM, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)







        


        
