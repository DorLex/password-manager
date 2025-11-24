from rest_framework.generics import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnDict

from core.crypto import fernet

from password_manager.models import Password
from password_manager.serializers.password import PasswordInputSerializer, PasswordSerializer, PasswordUpdateSerializer


class PasswordService:
    def get_password(self, service_name: str) -> ReturnDict:
        password: Password = get_object_or_404(Password, service_name=service_name)

        password.password = self._decrypt_password(password.encrypted_password)

        serializer: PasswordSerializer = PasswordSerializer(password)
        return serializer.data

    def create_password(self, password_data: dict) -> ReturnDict:
        PasswordInputSerializer(data=password_data).is_valid(raise_exception=True)

        password_data['encrypted_password'] = self._encrypt_password(password_data['password'])
        del password_data['password']

        serializer: PasswordSerializer = PasswordSerializer(data=password_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data

    def update_password(self, service_name: str, password_data: dict) -> ReturnDict:
        PasswordUpdateSerializer(data=password_data).is_valid(raise_exception=True)

        password: Password = get_object_or_404(Password, service_name=service_name)

        password_data['encrypted_password'] = self._encrypt_password(password_data['password'])
        del password_data['password']

        serializer: PasswordSerializer = PasswordSerializer(password, password_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data

    def _encrypt_password(self, password: str) -> str:
        """Шифруем пароль"""
        return fernet.encrypt(password.encode()).decode()

    def _decrypt_password(self, encrypted_password: str) -> str:
        """Дешифруем пароль"""
        return fernet.decrypt(encrypted_password.encode()).decode()
