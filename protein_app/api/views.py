from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .serializers import RegisterUserSerializer
from rest_framework import generics, permissions
# from .serializers import ResearcherSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework import status
from .authentication import BearerAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth import authenticate

class AuthTokenView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data, context={'request': request})        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk
        })


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        # get token
        token = Token.objects.get(user=user)

        user_data = serializer.data
        user_data['token'] = token.key

        return JsonResponse(data=user_data, status=status.HTTP_201_CREATED)


class ResearcherView(RetrieveUpdateDestroyAPIView):

    """User/Researcher views"""

    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    authentication_classes = (BearerAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        
        obj = super().get_object()
        
        if self.request.user.pk != obj.pk:
            raise ValidationError("You cannot modify this object")

        return obj
    