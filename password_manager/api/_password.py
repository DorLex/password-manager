from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from encryption.decrypt import get_decrypt_data
from password_manager._services import check_service_exists
from password_manager.models import Password
from password_manager.serializers.password import PasswordSerializer


class ServicePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, _request: Request, service_name: str) -> Response:
        """Получаем пароль по имени сервиса"""

        service = get_object_or_404(Password, service_name=service_name)
        serializer = PasswordSerializer(service)

        decrypt_response_data = get_decrypt_data(serializer.data)

        return Response(decrypt_response_data)

    def post(self, request: Request, service_name: str) -> Response:
        """Создаём пароль"""

        service_exists = check_service_exists(service_name)
        if service_exists:
            return Response({'detail': 'service c таким именем уже есть'}, status.HTTP_400_BAD_REQUEST)

        # Используем шифрование, а не хеширование, что бы возвращать пароль клиенту в исходном виде.
        # Т. к. шифрование работает в обе стороны, а хеширование - только в одну.
        encrypt_data = get_encrypt_data(request.data)
        encrypt_data['service_name'] = service_name

        serializer = PasswordSerializer(data=encrypt_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        decrypt_response_data = get_decrypt_data(serializer.data)

        return Response(decrypt_response_data)

    def patch(self, request: Request, service_name: str) -> Response:
        """Заменяем существующий пароль"""

        encrypt_data = get_encrypt_data(request.data)

        service = get_object_or_404(Password, service_name=service_name)

        serializer = PasswordSerializer(service, encrypt_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        decrypt_response_data = get_decrypt_data(serializer.data)

        return Response(decrypt_response_data)
