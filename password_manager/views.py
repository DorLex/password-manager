from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from encryption.decrypt import get_decrypt_data, get_many_decrypt_data
from encryption.encrypt import get_encrypt_data
from .models import ServicePassword
from .serializers import ServicePasswordSerializer
from .services import get_service_by_service_name, get_services_ilike_service_name


class ServicePasswordAPIView(APIView):

    def get(self, request, service_name):
        """Получаем пароль по имени сервиса"""

        service = get_object_or_404(ServicePassword, service_name=service_name)
        serializer = ServicePasswordSerializer(service)

        decrypt_response_data = get_decrypt_data(serializer.data)

        return Response(decrypt_response_data)

    def post(self, request, service_name):
        """Создаём пароль/заменяем существующий пароль"""

        # Обычно изменение записей производится через PUT или PATCH.
        # Но создание и изменение через POST было в условиях тестового задания.

        # Используем шифрование, а не хеширование, что бы возвращать пароль клиенту в исходном виде.
        # Т. к. шифрование работает в обе стороны, а хеширование - только в одну.
        encrypt_data = get_encrypt_data(request.data)

        service = get_service_by_service_name(service_name)

        if service:
            serializer = ServicePasswordSerializer(service, encrypt_data, partial=True)
        else:
            encrypt_data['service_name'] = service_name
            serializer = ServicePasswordSerializer(data=encrypt_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        decrypt_response_data = get_decrypt_data(serializer.data)

        return Response(decrypt_response_data)


class ServicePasswordILikeAPIView(APIView):

    def get(self, request):
        """Проводим поиск по части названия службы и выдаём пароли с подходящими service_name"""

        service_name = request.GET.get('service_name')
        services = get_services_ilike_service_name(service_name)
        serializer = ServicePasswordSerializer(services, many=True)

        decrypt_response_data = get_many_decrypt_data(serializer.data)

        return Response(decrypt_response_data)
