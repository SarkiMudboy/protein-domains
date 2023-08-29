import factory
from .models import Pfam, Domain


class PfamFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Pfam

    domain_id = factory.Sequence(lambda n: 'PF101010%d' % n)
    description = 'This is a test description'


class DomainFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Domain

    pfam = factory.SubFactory(PfamFactory)
    description = 'This is a test description'