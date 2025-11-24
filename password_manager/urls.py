from django.urls import URLPattern, path

from .api.password import ServicePasswordViewSet

urlpatterns: list[URLPattern] = [
    # path('password/<slug:service_name>', ServicePasswordAPIView.as_view(), name='password_by_service_name'),
    # path('password/', ServicePasswordILikeAPIView.as_view(), name='password_ilike_service_name'),
    path(
        'passwords/',
        ServicePasswordViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            },
        ),
        name='passwords-list',
    ),
    path(
        'passwords/<slug:service_name>/',
        ServicePasswordViewSet.as_view(
            {
                'get': 'retrieve',
                'patch': 'update',
            },
        ),
        name='passwords-detail',
    ),
]
