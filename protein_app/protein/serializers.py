from rest_framework import serializers
from .models import *
from domain.serializers import DomainSerializer

class TaxaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxa
        fields = [
            'taxa_id',
            'clade',
            'genus',
            'species',
        ]

class ProteinSerializer(serializers.ModelSerializer):

    taxonomy = TaxaSerializer(read_only=True)
    domains = DomainSerializer(many=True, read_only=True)

    class Meta:
        model = Protein
        fields = [
            'protein_id',
            'sequence',
            'taxonomy',
            'length',
            'domains',
        ]


class ProteinListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Protein
        lookup_field = 'taxonomy.taxa_id'
        fields = ['id', 'protein_id']
