from rest_framework.generics import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList

from encryption.decrypt import decrypt_password
from encryption.encrypt import get_encrypted_password
from password_manager.models import Password
from password_manager.serializers.password import PasswordInputSerializer, PasswordSerializer


class PasswordService:
    def get_passwords(self) -> ReturnList:
        return []

    def get_password(self, service_name: str) -> ReturnDict:
        service: Password = get_object_or_404(Password, service_name=service_name)

        service.password = decrypt_password(service.encrypted_password)

        serializer: PasswordSerializer = PasswordSerializer(service)
        return serializer.data

    def create_password(self, password_data: dict) -> dict:
        PasswordInputSerializer(data=password_data).is_valid(raise_exception=True)

        password_data['encrypted_password'] = get_encrypted_password(password_data['password'])
        del password_data['password']

        serializer: PasswordSerializer = PasswordSerializer(data=password_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # decrypt_response_data = get_decrypt_data(serializer.data)
        # return decrypt_response_data

        return serializer.data

    def update_password(self, service_name: str, password_data: dict) -> ReturnDict:
        return {}
