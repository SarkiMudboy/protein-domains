# import Protein, Taxa models
from protein.models import *
from domain.models import *

# get auth user model
from django.contrib.auth import get_user_model

from django.core.management.base import BaseCommand, CommandError

import csv

# As stated in the django-extensions documentation, “This file must implement a run() function. This is what gets called when you run the script.


User = get_user_model()

class Command(BaseCommand):

    help = 'Enriches the protein data with taxa data'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):

        path = options['path'][0]
        print(path)

        # concatenates the root path to filename
        path = r'C:\Users\ihima\OneDrive\Desktop\protein\protein-domains\protein_app\resources' + f'\{str(path)}'
        print(path)

        # opens the csv file using 'with' context management structure

        with open(str(path)) as file:

            # pass file variable to the reader function
            reader = csv.reader(file)

            # get superuser 'ihima'
            superuser = User.objects.get(username='ihima')

            # loop over all rows in the CSV
            for row in reader:

                # For the first time, It returns a tuple, where the object at the first index is the Django model object that was created (if it didn’t exist in the database yet) or retrieved (if it already existed). The second element in the tuple is a boolean that returns True if the object was created and False otherwise

                try:
                    protein = Protein.objects.get(
                        owner=superuser,
                        protein_id=row[0],
                    )
                    
                    # if protein exixts the pfam and domain is retreived and 
                    # the protein model is enriched.

                    if protein:

                        taxa = Taxa.objects.get(taxa_id=row[1])
                        protein.taxonomy = taxa

                        # save the model
                        protein.save()

                        print(protein.taxonomy.taxa_id)

                except Exception as e:
                    raise CommandError('An exception occured: ' + str(e))

        self.stdout.write(self.style.SUCCESS(
            'Successfully saved file data...'))
