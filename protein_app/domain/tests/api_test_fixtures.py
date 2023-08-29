from ..factory import PfamFactory, DomainFactory
import factory

class APIData:

    def __init__(self):
        ...

    def get_pfam_data(self, *args, **kwargs):

        self.pfam = factory.build(dict, FACTORY_CLASS=PfamFactory)
        return self.pfam
    
    def get_domain_data(self, *args, **kwargs):
        self.domain = factory.build(dict, FACTORY_CLASS=DomainFactory)
        return self.domain

