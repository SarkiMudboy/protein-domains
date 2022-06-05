from rest_framework import serializers
from .models import *


class ProteinSerializer(serializers.ModelSerializer):

    taxonomy = TaxaSerializer(read_only=True)
    domains = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='description'
    )

    class Meta:
        model = Protein
        fields = [
            'protein_id',
            'sequence',
            'taxonomy',
            'length',
            'domains',
        ]


class TaxaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxa
        fields = [
            'taxa_id',
            'clade',
            'genus',
            'species',
        ]
