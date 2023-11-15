from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ServicePassword
from .serializers import ServicePasswordSerializer


class ServicePasswordAPIView(APIView):

    def get(self, request, service_name):
        service = get_object_or_404(ServicePassword, service_name=service_name)
        serializer = ServicePasswordSerializer(service)

        return Response(serializer.data)

    def post(self, request, service_name):
        data = request.data

        service = ServicePassword.objects.filter(service_name=service_name).first()

        if service:
            serializer = ServicePasswordSerializer(service, request.data, partial=True)
        else:
            data['service_name'] = service_name
            serializer = ServicePasswordSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class LikeServicePasswordAPIView(APIView):

    def get(self, request):
        service_name = request.GET.get('service_name')

        queryset = ServicePassword.objects.filter(service_name__icontains=service_name)[:1]
        service = get_object_or_404(queryset)

        serializer = ServicePasswordSerializer(service)

        return Response(serializer.data)
