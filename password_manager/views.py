from cryptography.fernet import Fernet
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ServicePassword
from .serializers import ServicePasswordSerializer

# key = Fernet.generate_key()
key = 'LL8a2Gae_mGRes2fK49DOhK1WCdB7JgdChoUWgWMZbM='

fernet = Fernet(key)


class ServicePasswordAPIView(APIView):

    def get(self, request, service_name):
        service = get_object_or_404(ServicePassword, service_name=service_name)
        serializer = ServicePasswordSerializer(service)

        response_data = serializer.data
        decrypt_pass = fernet.decrypt(serializer.data['password'].encode()).decode()
        response_data['password'] = decrypt_pass

        return Response(response_data)

    def post(self, request, service_name):
        data = request.data
        password = data.get('password')
        data['password'] = fernet.encrypt(password.encode()).decode()

        service = ServicePassword.objects.filter(service_name=service_name).first()

        if service:
            serializer = ServicePasswordSerializer(service, data, partial=True)
        else:
            data['service_name'] = service_name
            serializer = ServicePasswordSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = serializer.data
        decrypt_pass = fernet.decrypt(serializer.data['password'].encode()).decode()
        response_data['password'] = decrypt_pass

        return Response(response_data)


class ServicePasswordILikeAPIView(APIView):

    def get(self, request):
        service_name = request.GET.get('service_name')
        services = ServicePassword.objects.filter(service_name__icontains=service_name)
        serializer = ServicePasswordSerializer(services, many=True)

        return Response(serializer.data)
