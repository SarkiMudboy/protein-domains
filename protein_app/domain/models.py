from django.db import models

# Create your models here.


class Pfam(models.Model):
    domain_id = models.CharField(max_length=10)
    domain_description = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.domain_id


class Domain(models.Model):
    pfam = models.ForeignKey(Pfam, on_delete=models.CASCADE)
    start = models.IntegerField(default=0)
    stop = models.IntegerField(default=0)

    def __str__(self):
        return self.description
