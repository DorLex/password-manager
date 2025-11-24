from rest_framework import serializers

from password_manager.models import Password


class PasswordInputSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model: type[Password] = Password
        fields: tuple = (
            'service_name',
            'password',
        )


class PasswordSerializer(serializers.ModelSerializer):
    encrypted_password = serializers.CharField(write_only=True)
    password = serializers.CharField(read_only=True)

    class Meta:
        model: type[Password] = Password
        fields: str | tuple = '__all__'
