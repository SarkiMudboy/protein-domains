import factory
from models import Pfam, Domain


class PfamFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Domain

    domain_id = factory.Sequence(lambda n: 'PF0040%d' % n)
    description = 'This is a test description'


class DomainFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Domain

    pfam = factory.SubFactory(PfamFactory)
    description = 'This is a test description'