from .test_helpers import ProteinTestHelper
from django.urls import reverse
from rest_framework import status
from protein.models import Protein, Taxa


PROTEIN_URL = 'protein:protein-list'
PROTEIN_CREATE = reverse('protein:protein-create')
PROTEIN_GET = 'protein:protein-get'
PROTEIN_UPDATE = 'protein:protein-update'
PROTEIN_DELETE = 'protein:protein-delete'

# taxa

TAXA_URL = 'protein:taxa-get'
TAXA_CREATE = reverse('protein:taxa-create')
TAXA_UPDATE = 'protein:taxa-update'
TAXA_DELETE = 'protein:taxa-delete'


class ProteinTestCase(ProteinTestHelper):

    def test_unauthenticated_user_cannot_create_new_protein(self):

        protein_data = self.data.get_protein_data()
        protein_data['protein_id'] = 'A0A016S8J11'

        response = self.client.post(PROTEIN_CREATE, protein_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        with self.assertRaises(Protein.DoesNotExist):
            Protein.objects.get(protein_id=protein_data.get('protein_id'))

    def test_authenticated_user_can_create_new_protein(self):

        protein_data = self.data.get_protein_data()

        # temporary: replace later

        protein_data['protein_id'] = "A0A016S8J11"

        self.client.force_authenticate(user=self.user)

        response = self.client.post(PROTEIN_CREATE, data=protein_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # self.assertIn()

    def test_proteins_are_unique(self):

        protein = self.proteins[0]
        create_data = self.data.get_protein_data()
        create_data['protein_id'] = protein.protein_id

        self.client.force_authenticate(user=self.user)
        response = self.client.post(PROTEIN_CREATE, data=create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        protein = Protein.objects.filter(protein_id=protein.protein_id)
        self.assertNotEqual(len(protein), 2)


    def test_anon_user_cannot_perform_mod_operations(self):

        protein = self.proteins[0]

        # UPDATE
        update_data = self.data.get_protein_data()
        update_data['protein_id'] = "A0A016S8J11"

        endpoint = self.build_url(PROTEIN_UPDATE, protein_id=protein.protein_id)
        response = self.client.post(endpoint, data=update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        protein_obj = Protein.objects.get(pk=protein.pk)

        self.assertNotEqual(protein_obj.protein_id, update_data.get('protein_id'))

        # DELETE

        endpoint = self.build_url(PROTEIN_DELETE, protein_id=protein.protein_id)
        response = self.client.post(endpoint, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_anon_user_can_perform_read_operations(self):

        protein = self.create_protein_with_domains()

        endpoint = self.build_url(PROTEIN_GET, protein_id=protein.protein_id)
        response = self.client.get(endpoint, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        print(data)
        # self.assertIs(len(data['domains']), )