from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import *
from protein_app.mixins import BaseCustomView
from .serializers import ProteinSerializer, ProteinListSerializer, TaxaSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class ProteinListView(generics.ListCreateAPIView):

    queryset = Protein.objects.all()
    serializer_class = ProteinListSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'taxa_id'

    def get_queryset(self):
        taxomomy = get_object_or_404(Taxa, taxa_id=self.kwargs.get(self.lookup_field))
        qs = Protein.objects.filter(taxonomy=taxomomy)
        return qs

class ProteinView(BaseCustomView):

    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'protein_id'


class TaxaCreateView(generics.ListCreateAPIView):
    queryset = Taxa.objects.all()
    serializer_class = TaxaSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class TaxaView(BaseCustomView):

    queryset = Taxa.objects.all()
    serializer_class = TaxaSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'taxa_id'
    
