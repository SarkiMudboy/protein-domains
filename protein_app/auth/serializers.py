from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import Group


class RegisterUserSerializer(serializers.ModelSerializer):

	username = serializers.CharField(
		required=True,
		validators=[UniqueValidator(queryset=User.objects.all())]
		)

	is_researcher = serializers.BooleanField(
		write_only=True,
		required=True
		)

	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = User
		fields = ('username', 'password', 'password2', 'is_researcher')

	def validate(self, attrs):
		if attrs['password'] != attrs['password2']:
			raise serializers.ValidationError({'password': 'Passwords must match.'})

		return attrs

	def create(self, validated_data):

		user = User.objects.create(
			username=validated_data['username'],	
		)
		
		user.set_password(validated_data['password'])

		user.save()




