from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList


class PasswordService:
    def get_passwords(self) -> ReturnList:
        return []

    def get_password(self, service_name: str) -> ReturnDict:
        return {}

    def create_password(self, password_data: dict) -> ReturnDict:
        return {}

    def update_password(self, service_name: str, password_data: dict) -> ReturnDict:
        return {}
