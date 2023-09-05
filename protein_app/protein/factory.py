import factory
from .models import Protein, Taxa
from users.factory import UserFactory


class TaxaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Taxa

    taxa_id = factory.Sequence(lambda n: '5566%d' % n)
    clade = 'T'
    genus = 'genus'
    species = 'species'



class ProteinFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Protein

    owner = factory.SubFactory(UserFactory)
    protein_id = factory.Sequence(lambda n: 'A0A016S8J%d' %n)
    sequence = 'WRSDFEYRGHFVSXCGETDRF'
    taxonomy = factory.SubFactory(TaxaFactory)
    length = 392
    
    @factory.post_generation
    def domains(self, create, extracted, **kwargs):
        if not create or not extracted:
            return None
        
        self.domains.add(*extracted)



    