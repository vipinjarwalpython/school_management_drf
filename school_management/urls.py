from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("faculty/", include("faculty.urls")),
    path("faculty/api/", include("faculty.api.urls")),
    path("student/", include("student.urls")),
    path("student/api/", include("student.api.urls")),
]
