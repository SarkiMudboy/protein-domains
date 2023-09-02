from .test_helpers import ResearcherTestHelper
from django.urls import reverse
from rest_framework import status
import secrets
from django.contrib.auth.models import User
from unittest.mock import patch
from rest_framework_simplejwt.exceptions import TokenError
from django.utils.translation import gettext_lazy as _

REGISTER = reverse('researchers:auth_register')
LOGIN = reverse('researchers:login')
RESEARCHER = 'researchers:researcher'

OBTAIN_TOKEN_PAIR = reverse('researchers:token_obtain_pair')
REFRESH_TOKEN = reverse('researchers:token_refresh')
VERIFY_TOKEN = reverse('researchers:token_verify')


class ResearcherTestCase(ResearcherTestHelper):

    def test_researcher_can_create_account(self):

        user_data = self.user_data

        response = self.client.post(path=REGISTER, data=user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, 'User not created')
        
        # self.assertGreater(len(User.objects.all()), 1)

    def test_researcher_cannot_create_account_without_required_credentials(self):

        user_data = self.user_data.copy()
        user_data.pop('username')
        user_data.pop('email')

        response = self.client.post(REGISTER, user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email=self.user_data.get('email'))

        # without password
        user_data = self.user_data.copy()
        user_data.pop('password'), user_data.pop('password2')

        response = self.client.post(REGISTER, user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email=self.user_data.get('email'))

        # without password2

        user_data = self.user_data.copy()
        
        user_data.pop('password2')

        response = self.client.post(REGISTER, user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email=self.user_data.get('email'))


    def test_password_not_included_in_register_response(self):

        user_data = self.user_data

        response = self.client.post(path=REGISTER, data=user_data, format='json')

        self.assertNotIn('password', response.json())

    def test_researcher_can_get_tokens_after_sign_up(self):

        user_data = self.user_data

        response = self.client.post(path=REGISTER, data=user_data, format='json')

        self.assertIn('token', response.json())

    def test_researcher_cannot_create_account_with_username_or_email_that_exists(self):

        user = self.user

        email = user.email
        username = user.username

        user_data = self.user_data
        user_data.update({'email': email, 'username': username})

        response = self.client.post(REGISTER, user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_login(self):

        user = self.user

        username = user.username
        password = user.password

        login_data = {'username': username, 'password': self.test_password}
        
        response = self.client.post(LOGIN, login_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json().get('token'), self.user_auth_token.key)

    def test_user_cannot_modify_account_without_token_or_wrong_token(self): 

        user_id = self.user.pk

        mod_data = {'username': 'Jenny2022'}

        endpoint = self.build_url(endpoint=RESEARCHER, pk=user_id)
        
        response = self.client.patch(endpoint, mod_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        updated_user = User.objects.get(pk=user_id)

        self.assertNotEqual(updated_user.username, mod_data.get('username'))

        # wrong token

        token = secrets.token_urlsafe(40)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        
        response = self.client.patch(endpoint, mod_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        updated_user = User.objects.get(pk=user_id)

        self.assertNotEqual(updated_user.username, mod_data.get('username'))


    def test_user_can_modify_account(self):

        email = self.user.email

        token = self.user_auth_token

        user_id = self.user.pk

        mod_data = {'username': 'Jenny2022'}

        endpoint = self.build_url(endpoint=RESEARCHER, pk=user_id)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.key)
        
        response = self.client.patch(endpoint, mod_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_user = User.objects.get(pk=user_id)

        self.assertEqual(updated_user.username, mod_data.get('username'))

        # get

        response = self.client.get(endpoint, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json().get('email'), self.user.email)

        # delete

        response = self.client.delete(endpoint, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email=email)



        
class JWTTokenTestCase(ResearcherTestHelper):

    def test_user_cannot_acess_tokens_without_credentials(self):
        
        response = self.client.post(OBTAIN_TOKEN_PAIR, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # test user can get tokens

        user_data = self.user

        login_data = {'username': user_data.username, 'password': self.test_password}

        response = self.client.post(OBTAIN_TOKEN_PAIR, data=login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        token_data = response.json()

        self.assertIsNotNone(token_data.get('access')), self.assertIsNotNone(token_data.get('refresh'))

    def user_cannnot_refresh_token_without_token(self):
        
        # get tokens

        user_data = self.user

        login_data = {'username': user_data.username, 'password': self.test_password}

        response = self.client.post(OBTAIN_TOKEN_PAIR, data=login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        access_token, refresh_token = response.json().get('access'), response.json().get('refresh')

        # refresh without token
        response = self.client.post(REFRESH_TOKEN, {}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # with token
        response = self.client.post(REFRESH_TOKEN, {'refresh': refresh_token}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertNotEqual(access_token, response.json().get('access'))
    
    @patch('rest_framework_simplejwt.tokens.Token.for_user')
    def test_token_expiry(self, validate_mock):
        
        user_data = self.user

        login_data = {'username': user_data.username, 'password': self.test_password}

        response = self.client.post(OBTAIN_TOKEN_PAIR, data=login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        access_token, refresh_token = response.json().get('access'), response.json().get('refresh')

        # verify access token

        validate_mock.side_effect = TokenError(_("Token is invalid or expired"))

        response = self.client.post(VERIFY_TOKEN, {'token': access_token}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # token expired

        validate_mock.side_effect = TokenError(_("Token is invalid or expired"))

        response = self.client.post(REFRESH_TOKEN, {'refresh': refresh_token}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)




        


