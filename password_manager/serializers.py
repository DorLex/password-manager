from rest_framework import serializers

from password_manager.models import ServicePassword


class ServicePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePassword
        fields = '__all__'
