from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import ResearcherSerializer
from rest_framework import viewsets
from rest_framework.response import Response




class ResearcherViewSet(viewsets.ModelViewSet):

    """User/Researcher views"""

    queryset = User.objects.all()
    serializer_class = ResearcherSerializer