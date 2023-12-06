from password_manager.models import ServicePassword


def check_service_exists(service_name):
    service_exists = ServicePassword.objects.filter(service_name=service_name).exists()
    return service_exists


def get_services_ilike_service_name(service_name):
    services = ServicePassword.objects.filter(service_name__icontains=service_name)
    return services
