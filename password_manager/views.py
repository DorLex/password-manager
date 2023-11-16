from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from encryption.decrypt import get_decrypt_data
from encryption.encrypt import get_encrypt_data
from .models import ServicePassword
from .serializers import ServicePasswordSerializer
from .services import get_service_by_service_name, get_services_ilike_service_name


class ServicePasswordAPIView(APIView):

    def get(self, request, service_name):
        service = get_object_or_404(ServicePassword, service_name=service_name)
        serializer = ServicePasswordSerializer(service)

        response_data = get_decrypt_data(serializer.data)

        return Response(response_data)

    def post(self, request, service_name):
        data = get_encrypt_data(request.data)

        service = get_service_by_service_name(service_name)

        if service:
            serializer = ServicePasswordSerializer(service, data, partial=True)
        else:
            data['service_name'] = service_name
            serializer = ServicePasswordSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = get_decrypt_data(serializer.data)

        return Response(response_data)


class ServicePasswordILikeAPIView(APIView):

    def get(self, request):
        service_name = request.GET.get('service_name')
        services = get_services_ilike_service_name(service_name)
        serializer = ServicePasswordSerializer(services, many=True)

        return Response(serializer.data)
