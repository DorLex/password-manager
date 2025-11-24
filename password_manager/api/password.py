from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class ServicePasswordViewSet(ViewSet):
    permission_classes: tuple = (IsAuthenticated,)

    def list(self, request: Request) -> Response[list]:
        return Response([])

    def create(self, request: Request) -> Response[dict]:
        return Response({})

    def retrieve(self, request: Request, service_name: str) -> Response[dict]:
        return Response({})

    def update(self, request: Request, service_name: str) -> Response[dict]:
        return Response({})
