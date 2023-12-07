from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Faculty(models.Model):
    faculty = models.ForeignKey(
        User, verbose_name=("Faculty"), on_delete=models.CASCADE
    )

    def __str__(self):
        return self.faculty.first_name
