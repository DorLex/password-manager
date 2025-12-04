from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from password_manager.models import Password
from password_manager.services.password import PasswordService

User: type[UserModel] = get_user_model()


class TestPassword(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user: User = User.objects.create_user(
            username='user_1',
            password='password_user_1',
        )

        cls.service_name: str = 'service_name_1'
        cls.password: str = 'password_service_1'
        cls.encrypt_data: dict = {
            'user_id': cls.user.pk,
            'service_name': cls.service_name,
            'encrypted_password': PasswordService()._encrypt_password(cls.password),
        }
        Password.objects.create(**cls.encrypt_data)

    def setUp(self) -> None:
        self.client.force_authenticate(user=self.user)

    def test_get_password(self) -> None:
        url: str = reverse('passwords-detail', args=[self.service_name])

        response: Response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['service_name'] == self.service_name
        assert response.data['password'] == self.password

    def test_create_password(self) -> None:
        service_name: str = 'service_name_2'
        password: str = 'password_service_name_2'

        url: str = reverse('passwords-list')
        body: dict = {
            'service_name': service_name,
            'password': password,
        }
        response: Response = self.client.post(url, data=body)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['service_name'] == service_name

    def test_update_password(self) -> None:
        new_password: str = 'new_password_service_1'

        url: str = reverse('passwords-detail', args=[self.service_name])
        body: dict = {'password': new_password}
        response: Response = self.client.patch(url, data=body)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['service_name'] == self.service_name
        password_obj: Password = Password.objects.get(service_name=self.service_name)
        assert new_password == PasswordService()._decrypt_password(password_obj.encrypted_password)
