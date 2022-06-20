from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import *
from .serializers import ProteinSerializer, ProteinListSerializer  
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class ProteinListView(generics.ListCreateAPIView):

    queryset = Protein.objects.all()
    serializer_class = ProteinListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'taxonomy.taxa_id'

    # def get_queryset(self):
    #     taxomomy = get_object_or_404(Taxomomy, taxa_id=lookup_field)
    #     qs = Protein.objects.filter(taxomomy=taxomomy)
    #     return qs


class ProteinRetrieveView(generics.RetrieveAPIView):

    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'protein_id'