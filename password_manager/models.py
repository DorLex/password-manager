from django.db import models


class ServicePassword(models.Model):
    service_name = models.CharField(max_length=255, unique=True, db_index=True)
    password = models.TextField()

    def __str__(self):
        return self.service_name
