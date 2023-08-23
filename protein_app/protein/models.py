from django.db import models
from domain.models import Domain
# Create your models here.


class Protein(models.Model):

    owner = models.ForeignKey(
        'auth.User', related_name='proteins', 
        null=True, blank=True, 
        on_delete=models.CASCADE
        )
    protein_id = models.CharField(max_length=20)
    sequence = models.CharField(max_length=90000)
    taxonomy = models.ForeignKey('Taxa', null=True, blank=True, on_delete=models.SET_NULL)
    length = models.IntegerField(default=0, null=True, blank=True)
    domains = models.ManyToManyField(Domain, null=True, blank=True)

    def get_taxa_id(self):
        return self.taxonomy.taxa_id

    def __str__(self):
        return self.protein_id


class Taxa(models.Model):

    taxa_id = models.CharField(max_length=10, unique=True)
    clade = models.CharField(max_length=1)
    genus = models.CharField(max_length=500)
    species = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "taxon"

    def __str__(self):
        return self.taxa_id
