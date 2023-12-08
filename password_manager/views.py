from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from encryption.decrypt import get_decrypt_data, get_many_decrypt_data
from encryption.encrypt import get_encrypt_data
from .models import ServicePassword
from .serializers import ServicePasswordSerializer
from .services import check_service_exists, get_services_ilike_service_name
from .validators import validate_get_parameters


class ServicePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, service_name):
        """Получаем пароль по имени сервиса"""

        service = get_object_or_404(ServicePassword, service_name=service_name)
        serializer = ServicePasswordSerializer(service)

        decrypt_response_data = get_decrypt_data(serializer.data)

        return Response(decrypt_response_data)

    def post(self, request, service_name):
        """Создаём пароль"""

        service_exists = check_service_exists(service_name)
        if service_exists:
            return Response({'detail': 'service c таким именем уже есть'}, status.HTTP_400_BAD_REQUEST)

        # Используем шифрование, а не хеширование, что бы возвращать пароль клиенту в исходном виде.
        # Т. к. шифрование работает в обе стороны, а хеширование - только в одну.
        encrypt_data = get_encrypt_data(request.data)
        encrypt_data['service_name'] = service_name

        serializer = ServicePasswordSerializer(data=encrypt_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        decrypt_response_data = get_decrypt_data(serializer.data)

        return Response(decrypt_response_data)

    def patch(self, request, service_name):
        """Заменяем существующий пароль"""

        encrypt_data = get_encrypt_data(request.data)

        service = get_object_or_404(ServicePassword, service_name=service_name)

        serializer = ServicePasswordSerializer(service, encrypt_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        decrypt_response_data = get_decrypt_data(serializer.data)

        return Response(decrypt_response_data)


class ServicePasswordILikeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Поиск по фрагменту service name"""

        service_name = request.GET.get('service_name')

        validate_get_parameters(service_name)

        services = get_services_ilike_service_name(service_name)
        serializer = ServicePasswordSerializer(services, many=True)

        decrypt_response_data = get_many_decrypt_data(serializer.data)

        return Response(decrypt_response_data)
