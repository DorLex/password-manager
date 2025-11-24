from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from encryption.decrypt import get_decrypt_data
from encryption.encrypt import get_encrypt_data
from password_manager.models import Password
from password_manager.serializers.password import PasswordSerializer

User = get_user_model()


class TestMy(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='user_1',
            password='test1test1test1',
        )

        cls.data = {
            'password': 'test1test1test1',
            'service_name': 'service_name_1',
        }
        cls.encrypt_data = get_encrypt_data(cls.data)
        cls.service = Password.objects.create(**cls.encrypt_data)

        cls.decrypt_data = get_decrypt_data(cls.encrypt_data)

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_get_password_by_service_name(self):
        url = reverse('password_by_service_name', args=['service_name_1'])
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.decrypt_data, response.data)

    def test_add_password_by_service_name(self):
        service_name = 'service_name_2'
        password = 'test2test2test2'

        url = reverse('password_by_service_name', args=[service_name])
        response = self.client.post(url, data={'password': password}, format='json')

        service = Password.objects.get(service_name=service_name)
        serializer = PasswordSerializer(service)
        decrypt_response_data = get_decrypt_data(serializer.data)

        expected_data = {'password': password, 'service_name': service_name}

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, decrypt_response_data)

    def test_get_password_ilike_service_name(self):
        url = reverse('password_ilike_service_name') + '?service_name=serv'
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([self.decrypt_data], response.data)
