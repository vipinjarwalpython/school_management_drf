from django.urls import path
from student import views

urlpatterns = [
    path("", views.index, name="home"),
    path("update/<int:id>", views.student_update, name="update"),
    path("doupdate/<int:id>", views.student_doupdate, name="doupdate"),
    path("delete/<int:id>", views.student_delete, name="delete"),
    path("faculty_signup/", views.faculty_signup, name="signup"),
    path("faculty_login/", views.faculty_login, name="login"),
    path("faculty_logout/", views.faculty_logout, name="logout"),
]
