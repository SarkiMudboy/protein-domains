from rest_framework import serializers
from .models import *


class PfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pfam
        fields = [
            'domian-id',
            'domain_description',
        ]


class DomainSerializer(serializers.ModelSerializer):

    pfam = serializers.PfamSerializer(read_only=True)
    description = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='domain_description',
    )

    class Meta:
        model = Domain
        fields = [
            'pfam',
            'description',
            'start',
            'stop',
        ]