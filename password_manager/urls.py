from django.urls import URLPattern, path

from .views import ServicePasswordAPIView, ServicePasswordILikeAPIView

urlpatterns: list[URLPattern] = [
    path('password/<slug:service_name>', ServicePasswordAPIView.as_view(), name='password_by_service_name'),
    path('password/', ServicePasswordILikeAPIView.as_view(), name='password_ilike_service_name'),
]
