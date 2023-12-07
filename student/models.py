from django.db import models
from faculty.models import Faculty

# Create your models here.


class Student(models.Model):
    faculty = models.ForeignKey(
        Faculty, verbose_name=("Faculty"), on_delete=models.CASCADE
    )

    rollno = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile = models.IntegerField()
    image = models.ImageField(upload_to="profile/")
