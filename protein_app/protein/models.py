from django.db import models
from domain.models import Domain
# Create your models here.


class Protein(models.Model):
    protein_id = models.CharField(max_length=20)
    sequence = models.CharField(max_length=20)
    taxonomy = models.ForeignKey('Taxa', null=True, blank=True, on_delete=models.SET_NULL)
    length = models.IntegerField(default=0)
    domains = models.ManyToManyField(Domain)

    def __str__(self):
        return self.protein_id

class Taxa(models.Model):
    taxa_id = models.CharField(max_length=10, unique=True)
    clade = models.CharField(max_length=1)
    genus = models.CharField(max_length=50)
    species = models.CharField(max_length=50)

    def __str__(self):
        return self.taxa_id

