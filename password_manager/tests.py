from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from encryption.decrypt import get_decrypt_data
from encryption.encrypt import get_encrypt_data
from password_manager.models import ServicePassword


class TestMy(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            'password': 'test1test1test1',
            'service_name': 'service_name_1'
        }
        cls.encrypt_data = get_encrypt_data(cls.data)
        cls.service = ServicePassword.objects.create(**cls.encrypt_data)

        cls.decrypt_data = get_decrypt_data(cls.encrypt_data)

    def test_get_password_by_service_name(self):
        url = reverse('password_by_service_name', args=['service_name_1'])
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.decrypt_data, response.data)

    def test_add_password_by_service_name(self):
        url = reverse('password_by_service_name', args=['service_name_2'])
        response = self.client.post(url, data={'password': 'test2test2test2'})
