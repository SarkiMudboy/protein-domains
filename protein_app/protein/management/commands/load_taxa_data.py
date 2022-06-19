# import Protein, Taxa models
from protein.models import *

# import BaseCommand to handle the terminal commands 
from django.core.management.base import BaseCommand, CommandError

# imports the in-built csv module
import csv

# As stated in the django-extensions documentation, “This file must implement a run() function. This is what gets called when you run the script.


class Command(BaseCommand):

    help = 'Enriches the database from a pre-populated csv'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):

        path = options['path'][0]
        print(path)
        # opens the csv file using 'with' context management structure

        with open(str(path)) as file:

            # pass file variable to the reader function
            reader = csv.reader(file)

            # to skip the CSV headers,
            next(reader)

            # remove any instances that might be in the models tables
            Taxa.objects.all().delete()

            # loop over all rows in the CSV
            for row in reader:

                # For the first time, It returns a tuple, where the object at the first index is the Django model object that was created (if it didn’t exist in the database yet) or retrieved (if it already existed). The second element in the tuple is a boolean that returns True if the object was created and False otherwise
                

                # split taxa data to get genus and species
                taxa_data = row[3].split(' ')

                genus = taxa_data[0]
                species = taxa_data[1]

                try:
                    taxa, _ = Taxa.objects.get_or_create(
                        taxa_id=row[1],
                        clade=row[2],
                        genus=genus,
                        species=species
                    )
                    print(row, f'genus:{genus} spec:{species}')
                except Exception as e:
                    raise CommandError('An exception occured: ' + str(e))

                # saves the model instance
                taxa.save()

        self.stdout.write(self.style.SUCCESS('Successfully saved file data...'))

