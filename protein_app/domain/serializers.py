from rest_framework import serializers
from .models import *


class PfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pfam
        fields = [
            'id',
            'domain_id',
            'description',
        ]

class DomainSerializer(serializers.ModelSerializer):

    domain_pfam = PfamSerializer(source='pfam', read_only=True)

    class Meta:
        model = Domain
        fields = [
            'id',
            'pfam',
            'domain_pfam',
            'description',
            'start',
            'stop'
        ]


class DomainRetrieveSerializer(serializers.ModelSerializer):

    pfam = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='description',
    )

    class Meta:
        model = Domain
        fields = [
            'id',
            'pfam',
            'start',
            'stop',
        ]
