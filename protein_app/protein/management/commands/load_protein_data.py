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

    help = 'Enriches the database from a pre-populated csv'

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
                    protein, created = Protein.objects.get_or_create(
                        owner=superuser,
                        protein_id=row[0],
                    )
                    
                    # if protein exixts the pfam and domain is retreived and 
                    # the protein model is enriched.

                    if protein:

                        pfam = Pfam.objects.get(
                            domain_id=row[-4],
                            )

                        domain = Domain.objects.filter(
                            pfam=pfam, 
                            start=row[-3],
                            stop=row[-2]
                            )

                        protein.length = row[-1]

                        # save the model
                        protein.save()

                        # clear all instances of the domains and enrich
                        protein.domains.clear()
                        protein.domains.add(*domain)

                        print(protein.id, [domain for domain in protein.domains.all()])

                except Exception as e:
                    raise CommandError('An exception occured: ' + str(e))

        self.stdout.write(self.style.SUCCESS(
            'Successfully saved file data...'))
