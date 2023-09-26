from .test_helpers import ProteinTestHelper
from django.urls import reverse
from rest_framework import status
from protein.models import Protein, Taxa
from django.shortcuts import get_object_or_404


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
        response = self.client.put(endpoint, data=update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        protein_obj = Protein.objects.get(pk=protein.pk)

        self.assertNotEqual(protein_obj.protein_id, update_data.get('protein_id'))

        # DELETE

        endpoint = self.build_url(PROTEIN_DELETE, protein_id=protein_obj.protein_id)
        response = self.client.delete(endpoint, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_anon_user_can_perform_read_operations(self):

        protein = self.create_protein_with_domains()
        
        endpoint = self.build_url(PROTEIN_GET, protein_id=protein.protein_id)
        response = self.client.get(endpoint, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        
        self.assertEqual(data['id'], protein.pk)
        self.assertEqual(data['protein_id'], protein.protein_id)
        self.assertEqual(data['taxonomy']['id'], protein.taxonomy.id)
        self.assertIs(len(data['domains']), len(protein.domains.all()))

        taxonomy = self.taxa[0]
        for protein in self.proteins:
            protein.taxonomy = taxonomy
            protein.save()

        endpoint = self.build_url(PROTEIN_URL, taxa_id=taxonomy.taxa_id)
        response = self.client.get(endpoint, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(data['count'], len(self.proteins))

    def test_authenticated_user_can_perform_mod_ops(self):
        
        protein = self.proteins[0]

        # UPDATE
        update_data = self.data.get_protein_data()
        update_data['protein_id'] = "A0A016S8J11"

        endpoint = self.build_url(PROTEIN_UPDATE, protein_id=protein.protein_id)

        self.client.force_authenticate(user=self.user)
        response = self.client.put(endpoint, data=update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        protein_obj = Protein.objects.get(pk=protein.pk)

        self.assertEqual(protein_obj.protein_id, update_data.get('protein_id'))

        # DELETE

        endpoint = self.build_url(PROTEIN_DELETE, protein_id=protein_obj.protein_id)
        response = self.client.delete(endpoint, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Protein.DoesNotExist):
            Protein.objects.get(pk=protein.pk)


class TaxaTestCase(ProteinTestHelper):
    
    def test_unauthenticated_user_cannot_create_new_taxa(self):

        taxa_data = self.data.get_taxa_data()
        taxa_data['taxa_id'] = '5454545'

        response = self.client.post(TAXA_CREATE, taxa_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        with self.assertRaises(Taxa.DoesNotExist):
            Taxa.objects.get(taxa_id=taxa_data.get('taxa_id'))