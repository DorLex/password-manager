from django.urls import path

from .views import ServicePasswordAPIView, ServicePasswordILikeAPIView

urlpatterns = [
    path('password/<slug:service_name>', ServicePasswordAPIView.as_view(), name='password_by_service_name'),
    path('password/', ServicePasswordILikeAPIView.as_view(), name='password_ilike_service_name'),
]
