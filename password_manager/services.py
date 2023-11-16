from password_manager.models import ServicePassword


def get_service_by_service_name(service_name):
    service = ServicePassword.objects.filter(service_name=service_name).first()
    return service


def get_services_ilike_service_name(service_name):
    services = ServicePassword.objects.filter(service_name__icontains=service_name)
    return services
