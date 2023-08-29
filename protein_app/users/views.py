from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import ResearcherSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError


# class CreateResearcherView(CreateAPIView):
#     """Creating researcher"""

#     queryset = User.objects.all()
#     serializer_class = ResearcherSerializer


# class ResearcherView(RetrieveUpdateDestroyAPIView):

#     """User/Researcher views"""

#     queryset = User.objects.all()
#     serializer_class = ResearcherSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]

#     def get_object(self):
        
#         obj = super().get_object()

#         if self.request.user.pk != obj.pk:
#             raise ValidationError("You cannot modify this object")

#         return obj

        
