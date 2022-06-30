# import Pfam, Domain models
from domain.models import *

# import BaseCommand to handle the terminal commands
from django.core.management.base import BaseCommand, CommandError

# imports the in-built csv module
import csv

# As stated in the django-rest documentation, “This file must implement a handle() function. This is what gets called when you run the script.


class Command(BaseCommand):

    help = 'Enriches the database from a pre-populated csv'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):

        path = options['path'][0]
        print(path)

        # concatenates the root path to filename
        path = 'C:/Users/Abdul/Desktop/protein/protein-domains/protein_app/resources/' + \
            str(path)

        # opens the csv file using 'with' context management structure

        with open(str(path)) as file:

            # pass file variable to the reader function
            reader = csv.reader(file)

            # to skip the CSV headers,
            next(reader)

            # remove any instances that might be in the models tables
            # Protein.objects.all().delete()

            # loop over all rows in the CSV
            for row in reader:

                # For the first time, It returns a tuple, where the object at the first index is the Django model object that was created (if it didn’t exist in the database yet) or retrieved (if it already existed). The second element in the tuple is a boolean that returns True if the object was created and False otherwise

                try:
                    pfam = Pfam.objects.get(
                        domain_id=row[-4],
                    )

                    if pfam:

                        print(pfam.domain_id)

                        domain = Domain.objects.filter(
                            pfam=pfam,
                            start=row[-3],
                            stop=row[-2],
                        )

                        for d in domain:
                            d.delete()

                        # domain.description = row[-5]

                        # saves the model instance
                        # domain.save()

                except Exception as e:
                    raise CommandError('An exception occured: ' + str(e))

        self.stdout.write(self.style.SUCCESS(
            'Successfully saved file data...'))
