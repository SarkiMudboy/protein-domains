from ..factory import ProteinFactory, TaxaFactory
import factory

class APIData:

    def __init__(self):
        ...

    def get_taxa_data(self, *args, **kwargs):

        self.taxa = factory.build(dict, FACTORY_CLASS=TaxaFactory)
        return self.taxa
    
    def get_protein_data(self, *args, **kwargs):
        
        self.protein = factory.build(dict, FACTORY_CLASS=ProteinFactory)

        user = self.protein.pop('owner')
        user.save()
        self.protein['owner'] = user.id

        # save taxa to persist it to db and get an id
        taxa = self.protein.pop('taxonomy')
        taxa.save()
        self.protein['taxonomy'] = taxa.id

        return self.protein

