from django.urls import path
from faculty.api.views import *

urlpatterns = [
    path("show/", FacultyAPI.as_view()),
    path("show/<int:id>/", FacultyAPI.as_view()),
]
