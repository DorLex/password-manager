from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from rest_framework.viewsets import ViewSet

from password_manager.serializers.password import PasswordInputSerializer
from password_manager.services.password import PasswordService


class PasswordViewSet(ViewSet):
    permission_classes: tuple = (IsAuthenticated,)

    def list(self, _request: Request) -> Response[list]:
        password_service: PasswordService = PasswordService()
        passwords: ReturnList = password_service.get_passwords()
        return Response(passwords)

    @extend_schema(request=PasswordInputSerializer)
    def create(self, request: Request) -> Response[dict]:
        """Сохранить пароль для сервиса"""

        password_service: PasswordService = PasswordService()
        password: ReturnDict = password_service.create_password(request.data)
        return Response(password, status=status.HTTP_201_CREATED)

    def retrieve(self, _request: Request, service_name: str) -> Response[dict]:
        """Получаем пароль по имени сервиса"""

        password_service: PasswordService = PasswordService()
        password: ReturnDict = password_service.get_password(service_name)
        return Response(password)

    def update(self, request: Request, service_name: str) -> Response[dict]:
        password_service: PasswordService = PasswordService()
        password: ReturnDict = password_service.update_password(service_name, request.data)
        return Response(password)
