from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from encryption.decrypt import get_many_decrypt_data
from password_manager._services import get_services_ilike_service_name
from password_manager.serializers.password import PasswordSerializer
from password_manager.validators import validate_get_parameters


class ServicePasswordILikeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        """Поиск по фрагменту service name"""

        service_name = request.GET.get('service_name')

        validate_get_parameters(service_name)

        services = get_services_ilike_service_name(service_name)
        serializer = PasswordSerializer(services, many=True)

        decrypt_response_data = get_many_decrypt_data(serializer.data)

        return Response(decrypt_response_data)
