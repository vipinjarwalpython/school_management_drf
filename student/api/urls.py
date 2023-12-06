from django.urls import path
from student.api.views import *

urlpatterns = [
    path("show/", StudentAPI.as_view()),
    path("show/<int:id>/", StudentAPI.as_view()),
]
