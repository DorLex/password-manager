from django.urls import URLPattern, path

from password_manager.api.password import PasswordViewSet

urlpatterns: list[URLPattern] = [
    path('passwords/', PasswordViewSet.as_view({'post': 'create'}), name='passwords-list'),
    path(
        'passwords/<slug:service_name>/',
        PasswordViewSet.as_view(
            {
                'get': 'retrieve',
                'patch': 'update',
            },
        ),
        name='passwords-detail',
    ),
]
