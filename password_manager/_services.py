from django.db.models import QuerySet

from password_manager.models import Password


def check_service_exists(service_name: str) -> bool:
    service_exists = Password.objects.filter(service_name=service_name).exists()
    return service_exists


def get_services_ilike_service_name(service_name: str) -> QuerySet[Password]:
    services = Password.objects.filter(service_name__icontains=service_name)
    return services
