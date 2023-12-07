from django.urls import path
from student import views

urlpatterns = [
    path("", views.index, name="home"),
    path("update/<int:id>", views.student_update, name="update"),
    path("doupdate/<int:id>", views.student_doupdate, name="doupdate"),
    path("delete/<int:id>", views.student_delete, name="delete"),
]
