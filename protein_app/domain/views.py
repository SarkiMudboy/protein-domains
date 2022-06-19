from .models import *
from .serializers import PfamSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class PfamListView(generics.ListCreateAPIView):
    queryset = Pfam.objects.all()
    serializer_class = PfamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PfamRetrieveView(generics.RetrieveAPIView):
    queryset = Pfam.objects.all()
    serializer_class = PfamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'domain_id'
