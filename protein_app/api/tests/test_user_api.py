from .test_helpers import ResearcherTestHelper
from django.urls import reverse
from rest_framework import status
import secrets
from django.conf import settings


REGISTER = reverse('researchers:auth_register')
LOGIN = reverse('researchers:login')
RESEARCHER = 'researchers:researcher'

User = settings.AUTH_USER_MODEL

class ResearcherTestcase(ResearcherTestHelper):

    def test_researcher_can_create_account(self):

        user_data = self.user_data

        response = self.client.post(path=REGISTER, data=user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, 'User not created')

    def test_researcher_cannot_create_account_without_required_credentials(self):

        user_data = self.user_data.copy()
        user_data.pop('username')
        user_data.pop('email')

        response = self.client.post(REGISTER, user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # without password

        user_data = self.user_data.copy()
        user_data.pop('password'), user_data.pop('password2')

        response = self.client.post(REGISTER, user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # without password2

        user_data = self.user_data.copy()
        
        user_data.pop('password2')

        response = self.client.post(REGISTER, user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


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

        login_data = {'username': username, 'password': password}

        response = self.client.post(LOGIN, login_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json().get('token'), self.user_auth_token)

    def test_user_cannot_modify_account_without_token_or_wrong_token(self): 

        user_id = self.user.pk

        mod_data = {'username': 'Jenny2022'}

        endpoint = self.build_url(endpoint=RESEARCHER, pk=user_id)
        
        response = self.client.patch(endpoint, mod_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # wrong token

        token = secrets.token_urlsafe(40)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        
        response = self.client.patch(endpoint, mod_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_user_can_modify_account(self):

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
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


        # self.assertEqual()



        



        


