# import Protein, Taxa models as well as Domain and Pfam models

from protein.models import *
from domain.models import *

# imports the in-built csv module
import csv

# As stated in the django-extensions documentation, “This file must implement a run() function. This is what gets called when you run the script.
def run():

    # opens the csv file using 'with' context management structure
    with open('resources/pfam_descriptions.csv') as file:

        # pass file variable to the reader function
        reader = csv.reader(file)

        # to skip the CSV headers,
        next(reader)

        # remove any instances that might be in the models tables
        Pfam.objects.all().delete()

        # loop over all rows in the CSV
        for row in reader:
            print(row)

            # For the first time, It returns a tuple, where the object at the first index is the Django model object that was created (if it didn’t exist in the database yet) or retrieved (if it already existed). The second element in the tuple is a boolean that returns True if the object was created and False otherwise
            pfam, _ = Pfam.objects.get_or_create(domain_id=row[-1], domain_description=row[-2])

            # saves the model instance
            pfam.save()