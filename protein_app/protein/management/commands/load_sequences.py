# import Protein, Taxa models
from protein.models import *
from domain.models import *
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

import csv

# As stated in the django-extensions documentation, “This file must implement a run() function. This is what gets called when you run the script.


User = get_user_model()

class Command(BaseCommand):

    help = 'Enriches the database from a pre-populated csv: initial injection for protein and its sequences'

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

            # delete any instances that is still in the model tables
            # Protein.objects.all().delete()

            # loop over all rows in the CSV
            for row in reader:

                # For the first time, It returns a tuple, where the object at the first index is the Django model object that was created (if it didn’t exist in the database yet) or retrieved (if it already existed). The second element in the tuple is a boolean that returns True if the object was created and False otherwise

                try:
                    protein = Protein.objects.get(
                        owner=superuser,
                        protein_id=row[0],
                        sequence=row[1]
                    )

                    # saves the protein
                    protein.save()

                    print(protein.id, protein.sequence)

                except Exception as e:
                    raise CommandError('An exception occured: ' + str(e))

        self.stdout.write(self.style.SUCCESS(
            'Successfully saved file data...'))
