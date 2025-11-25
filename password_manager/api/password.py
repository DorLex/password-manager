from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.viewsets import ViewSet

from password_manager.serializers.password import (
    PasswordCreateInputSerializer,
    PasswordResponseSerializer,
    PasswordSaveSerializer,
    PasswordUpdateInputSerializer,
)
from password_manager.services.password import PasswordService


@extend_schema(tags=['Passwords'])
class PasswordViewSet(ViewSet):
    permission_classes: tuple = (IsAuthenticated,)

    @extend_schema(
        request=PasswordCreateInputSerializer,
        responses=PasswordSaveSerializer,
    )
    def create(self, request: Request) -> Response[dict]:
        """Сохранить пароль для сервиса."""
        password_service: PasswordService = PasswordService()
        password: ReturnDict = password_service.create_password(request.data)
        return Response(password, status=status.HTTP_201_CREATED)

    @extend_schema(responses=PasswordResponseSerializer)
    def retrieve(self, _request: Request, service_name: str) -> Response[dict]:
        """Получить пароль по имени сервиса."""
        password_service: PasswordService = PasswordService()
        password: ReturnDict = password_service.get_raw_password(service_name)
        return Response(password)

    @extend_schema(
        request=PasswordUpdateInputSerializer,
        responses=PasswordSaveSerializer,
    )
    def update(self, request: Request, service_name: str) -> Response[dict]:
        """Обновить пароль для сервиса."""
        password_service: PasswordService = PasswordService()
        password: ReturnDict = password_service.update_password(service_name, request.data)
        return Response(password)
