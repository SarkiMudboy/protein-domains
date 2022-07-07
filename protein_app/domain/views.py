from .models import *
from django.shortcuts import get_object_or_404
from protein_app.mixins import BaseCustomView
from .serializers import PfamSerializer, DomainSerializer, DomainRetrieveSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions


class PfamListView(generics.ListCreateAPIView):
    queryset = Pfam.objects.all()
    serializer_class = PfamSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticatedOrReadOnly]

class PfamTaxaListView(generics.ListAPIView):
    queryset = Pfam.objects.all()
    serializer_class = PfamSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticatedOrReadOnly]
    lookup_url_kwarg = 'taxa_id'

    def get_queryset(self):
        taxa_id = self.kwargs.get(self.lookup_url_kwarg)
        qs = Pfam.objects.filter(domain__protein__taxonomy__taxa_id=taxa_id)
        return qs

class PfamView(BaseCustomView):
    queryset = Pfam.objects.all()
    serializer_class = PfamSerializer
    lookup_field = 'domain_id'


class DomainListView(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = Domain.objects.prefetch_related('pfam')
        return qs

class DomainView(BaseCustomView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    lookup_field = 'id'



