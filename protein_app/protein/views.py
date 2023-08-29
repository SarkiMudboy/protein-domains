from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import *
from protein_app.mixins import BaseCustomView
from .serializers import ProteinSerializer, ProteinListSerializer, TaxaSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly, IsAuthenticated


class ProteinListView(generics.ListCreateAPIView):

    queryset = Protein.objects.all()
    serializer_class = ProteinListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'taxa_id'

    def get_queryset(self):
        taxomomy = get_object_or_404(Taxa, taxa_id=self.request.data.get(self.lookup_field))
        qs = Protein.objects.filter(taxonomy=taxomomy)
        return qs

    def get_user(self):
        return self.request.user

    def perform_create(self, serializer):
        """set the sender to the logged in user"""
        serializer.save(owner=self.get_user())


class ProteinView(BaseCustomView):

    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer
    lookup_field = 'protein_id'


class TaxaCreateView(generics.ListCreateAPIView):
    queryset = Taxa.objects.all()
    serializer_class = TaxaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TaxaView(BaseCustomView):

    queryset = Taxa.objects.all()
    serializer_class = TaxaSerializer
    lookup_field = 'taxa_id'
    
