from .models import *
from serializers import PfamSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class PfamListView(generics.ListCreateAPIView):
    query_set = Pfam.objects.all()
    serializer_class = PfamSerializer
    permission_classes = [IsAdminUser]
