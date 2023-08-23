from rest_framework import serializers
from django.contrib.auth.models import User

class ResearcherSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    