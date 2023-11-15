from django.urls import path

from .views import ServicePasswordAPIView, ServicePasswordILikeAPIView

urlpatterns = [
    path('password/<slug:service_name>', ServicePasswordAPIView.as_view()),
    path('password/', ServicePasswordILikeAPIView.as_view()),
]
