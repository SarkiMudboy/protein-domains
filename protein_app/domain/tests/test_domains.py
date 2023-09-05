from .test_helpers import DomainTestHelper
from django.urls import reverse
from rest_framework import status
from domain.models import Pfam, Domain
from protein.factory import ProteinFactory


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

        # temporary: replace later

        pfam_data['domain_id'] = "PF10101099"

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

    def test_pfams_are_unique(self):

        pfam = self.pfams[0]
        create_data = {
            'domain_id': pfam.domain_id,
            'description': 'this is a test description'
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(PFAM_URL, data=create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        pfams = Pfam.objects.filter(domain_id=pfam.domain_id)
        self.assertNotEqual(len(pfams), 2)

    def test_anon_user_cannot_perform_mod_operations(self):

        pfam = self.pfams[0]

        # UPDATE

        update_data = {'domain_id': 'PF033423', 'description': 'updated description'}

        endpoint = self.build_url(PFAM_UPDATE, domain_id=pfam.domain_id)
        
        response = self.client.post(endpoint, data=update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        pfam_obj = Pfam.objects.get(pk=pfam.pk)

        self.assertNotEqual(pfam_obj.domain_id, update_data.get('domain_id'))

        # DELETE

        endpoint = self.build_url(PFAM_DELETE, domain_id=pfam.domain_id)

        response = self.client.post(endpoint, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_anon_user_can_perform_read_operations(self):

        pfam = self.pfams[0]

        endpoint = self.build_url(GET_PFAM, domain_id=pfam.domain_id)

        response = self.client.get(endpoint, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        self.assertEqual(data.get('domain_id'), pfam.domain_id)

        # get interface protein 

        domains = self.domains
        pfams = [domain.pfam for domain in domains]

        protein = ProteinFactory.create(domains=domains)
        taxa = protein.taxonomy

        endpoint = self.build_url(PFAM_GET_TAXA_URL, taxa_id=taxa.taxa_id)

        response = self.client.get(endpoint, format='json')
        data = response.json()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], len(pfams))

        # get all pfam
        response = self.client.get(PFAM_URL, format='json')
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], 20)

    def test_authenticated_user_can_perform_mod_operations(self):

        pfam = self.pfams[0]

        # UPDATE

        update_data = {'domain_id': 'PF033423', 'description': 'updated description'}

        endpoint = self.build_url(PFAM_UPDATE, domain_id=pfam.domain_id)
        
        self.client.force_authenticate(user=self.user)
        response = self.client.put(endpoint, data=update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        pfam_obj = Pfam.objects.get(pk=pfam.pk)
        self.assertEqual(pfam_obj.domain_id, update_data.get('domain_id'))

        # DELETE

        endpoint = self.build_url(PFAM_DELETE, domain_id=pfam.domain_id)
        
        response = self.client.delete(endpoint, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        with self.assertRaises(Pfam.DoesNotExist):
            Pfam.objects.get(id=pfam.pk)
        
