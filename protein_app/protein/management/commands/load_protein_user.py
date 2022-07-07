# import Protein, Taxa models
from protein.models import *
from domain.models import *
from django.contrib.auth.models import User

# import BaseCommand to handle the terminal commands
from django.core.management.base import BaseCommand, CommandError

# imports the in-built csv module
import csv

# As stated in the django-extensions documentation, “This file must implement a run() function. This is what gets called when you run the script.


class Command(BaseCommand):

    help = 'Assigns the superuser as owner to existing protein models'

    def add_arguments(self, parser):
        parser.add_argument('user', nargs='+', type=str)

    def handle(self, *args, **options):

        user = options['user'][0]
        user = str(user)

        try:

            superuser = User.objects.get(username=user)
            proteins = Protein.objects.all()

            for protein in proteins:

                protein.owner = superuser
                print(protein.protein_id, protein.owner)

                protein.save()

        except Exception as e:
            raise CommandError('An exception occured: ' + str(e))

        self.stdout.write(self.style.SUCCESS(
            'Successfully saved file data...'))
