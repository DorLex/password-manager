from django.urls import path

from .views import ServicePasswordAPIView, LikeServicePasswordAPIView

urlpatterns = [
    path('password/<slug:service_name>', ServicePasswordAPIView.as_view()),
    path('password/', LikeServicePasswordAPIView.as_view()),
]
