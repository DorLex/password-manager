from django.db import models


class Password(models.Model):
    service_name = models.CharField(max_length=255, unique=True, db_index=True)
    encrypted_password = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.service_name
