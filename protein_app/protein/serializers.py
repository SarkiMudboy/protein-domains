from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *
from domain.serializers import DomainSerializer
from abstract.api.nbci_api import fetch_taxa


class TaxaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxa
        fields = [
            'id',
            'taxa_id',
            'clade',
            'genus',
            'species',
        ]

    def validate(self,data):

        result = fetch_taxa(data['taxa_id'])
        instance_data = data['genus'], data['species']

        if result and instance_data == result:
            return data
        raise serializers.ValidationError('Invalid parameters')

class ProteinSerializer(serializers.ModelSerializer):

    taxonomy = TaxaSerializer(read_only=True)
    domains = DomainSerializer(many=True, read_only=True)

    class Meta:
        model = Protein
        fields = [
            'id',
            'protein_id',
            'sequence',
            'taxonomy',
            'length',
            'domains',
        ]


class ProteinListSerializer(serializers.ModelSerializer):

    protein_id = serializers.CharField(
        max_length=20, 
        validators=[UniqueValidator(queryset=Protein.objects.prefetch_related('taxonomy'))]
        )

    class Meta:
        model = Protein
        lookup_field = 'taxonomy.taxa_id'
        fields = ['id', 'protein_id', 'sequence']

    def validate_sequence(self, value):

        if not value.isupper():
            raise serializers.ValidationError(
                'The sequence characters must be uppercase')

        return value

