from rest_framework import serializers

from password_manager.models import Password


class PasswordCreateInputSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model: type[Password] = Password
        fields: tuple = (
            'service_name',
            'password',
        )


class PasswordUpdateSerializer(serializers.Serializer):
    password = serializers.CharField()


class PasswordSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[Password] = Password
        fields: str | tuple = '__all__'


class PasswordResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    service_name = serializers.CharField()
    password = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
