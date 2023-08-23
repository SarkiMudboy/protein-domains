import requests

def fetch_taxa(taxa_id):

    endpoint = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/taxonomy/taxid/{taxa_id}/summary/JSON'

    response = requests.get(endpoint)

    taxa_data = response.json()

    if 'Fault' in taxa_data:
        return False

    else:
        genus = taxa_data['TaxonomySummaries']['TaxonomySummary'][0]['RankedLineage']['Genus']
        species = taxa_data['TaxonomySummaries']['TaxonomySummary'][0]['RankedLineage']['Species']
        return genus, species
