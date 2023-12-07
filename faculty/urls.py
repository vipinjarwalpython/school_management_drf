from django.urls import path
from faculty import views

urlpatterns = [
    path("faculty_signup/", views.faculty_signup, name="signup"),
    path("faculty_login/", views.faculty_login, name="login"),
    path("faculty_logout/", views.faculty_logout, name="logout"),
]
