from rest_framework import serializers
from django.contrib.auth.models import User


class ResearcherSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):

        user = User(email=validated_data.get('email'),
                    username=validated_data.get('username'))
        
        user.set_password(validated_data.get('password'))

        user.save()

        return user

    

    