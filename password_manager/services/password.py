from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnDict

from core.crypto import fernet
from password_manager.models import Password
from password_manager.serializers.password import (
    PasswordCreateInputSerializer,
    PasswordResponseSerializer,
    PasswordSaveSerializer,
    PasswordUpdateInputSerializer,
)


class PasswordService:
    def get_raw_password(self, user: User, service_name: str) -> ReturnDict:
        password: Password = get_object_or_404(Password, user_id=user.pk, service_name=service_name)

        password.password = self._decrypt_password(password.encrypted_password)

        serializer: PasswordResponseSerializer = PasswordResponseSerializer(password)
        return serializer.data

    def create_password(self, user: User, password_data: dict) -> ReturnDict:
        PasswordCreateInputSerializer(data=password_data).is_valid(raise_exception=True)

        password_data['user'] = user.pk  # TODO: понять, можно ли удобнее
        password_data['encrypted_password'] = self._encrypt_password(password_data['password'])

        save_serializer: PasswordSaveSerializer = PasswordSaveSerializer(data=password_data)
        save_serializer.is_valid(raise_exception=True)
        save_serializer.save()
        return save_serializer.data

    def update_password(self, user: User, service_name: str, password_data: dict) -> ReturnDict:
        PasswordUpdateInputSerializer(data=password_data).is_valid(raise_exception=True)

        password: Password = get_object_or_404(Password, user_id=user.pk, service_name=service_name)

        password_data['encrypted_password'] = self._encrypt_password(password_data['password'])

        save_serializer: PasswordSaveSerializer = PasswordSaveSerializer(password, password_data, partial=True)
        save_serializer.is_valid(raise_exception=True)
        save_serializer.save()

        return save_serializer.data

    def _encrypt_password(self, password: str) -> str:
        """Зашифровать пароль."""
        return fernet.encrypt(password.encode()).decode()

    def _decrypt_password(self, encrypted_password: str) -> str:
        """Дешифровать пароль."""
        return fernet.decrypt(encrypted_password.encode()).decode()
