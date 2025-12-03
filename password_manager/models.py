from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

User: type[AbstractBaseUser] = get_user_model()


class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passwords')
    service_name = models.CharField(max_length=255, unique=True, db_index=True)
    encrypted_password = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.service_name
