from urllib import response
from django.shortcuts import render, redirect
from student.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from faculty.models import Faculty
import os
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


@login_required(login_url="/faculty/faculty_login/")
def index(request):
    try:
        if request.method == "POST":
            userid = request.user.id
            rollno = request.POST.get("rollno")
            name = request.POST.get("name").upper()
            age = request.POST.get("age")
            mobile = request.POST.get("mobile")
            image = request.FILES.get("image")

            # print(name)
            # print(username)
            # print("====================================================")

            # jumping foreign key access
            faculty = Faculty.objects.get(faculty=userid)
            # print(faculty)
            # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            student = Student.objects.create(
                faculty=faculty,
                rollno=rollno,
                name=name,
                age=age,
                mobile=mobile,
                image=image,
            )
            student.save()
            messages.success(request, "Student Registration is successfully")
            return redirect("/student/")
        # return render(request, "index.html")
        else:
            faculty = Faculty.objects.get(faculty=request.user.id)

            student = Student.objects.filter(faculty=faculty.id)

            return render(request, "index.html", {"student": student})

    except Exception as E:
        return Response(str(E), status=status.HTTP_400_BAD_REQUEST)


def student_update(request, id):
    student = Student.objects.get(pk=id)
    return render(request, "student_update.html", {"student": student})


def student_doupdate(request, id):
    try:
        if request.method == "POST":
            rollno = request.POST.get("rollno")
            name = request.POST.get("name").upper()
            age = request.POST.get("age")
            mobile = request.POST.get("mobile")
            image = request.FILES.get("image")
            # print(rollno, name)

        student = Student.objects.get(pk=id)
        path = student.image.path

        if image:
            student.image = image
            os.remove(path)
            student.save()

        student.rollno = rollno
        student.name = name
        student.age = age
        student.mobile = mobile
        student.save()
        return redirect("/student/")

    except Exception as E:
        return Response(str(E), status=status.HTTP_400_BAD_REQUEST)


def student_delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect("/student/")
