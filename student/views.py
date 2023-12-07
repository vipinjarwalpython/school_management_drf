from urllib import response
from django.shortcuts import render, redirect
from student.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from faculty.models import Faculty


# Create your views here.


@login_required(login_url="/faculty/faculty_login/")
def index(request):
    # try:
    if request.method == "POST":
        userid = request.user.id
        rollno = request.POST.get("rollno")
        name = request.POST.get("name").upper()
        age = request.POST.get("age")
        mobile = request.POST.get("mobile")
        image = request.FILES.get("image")

        # print(name)
        # print(username)
        print("====================================================")

        # jumping foreign key access
        faculty = Faculty.objects.get(faculty=userid)
        print(faculty)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

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
    else:
        student = Student.objects.all().values()
    # except Exception as E:
    #     return response(request(E))

    return render(request, "index.html", {"student": student})


def student_update(request, id):
    student = Student.objects.get(pk=id)
    return render(request, "student_update.html", {"student": student})


def student_doupdate(request, id):
    if request.method == "POST":
        rollno = request.POST.get("rollno")
        name = request.POST.get("name").upper()
        age = request.POST.get("age")
        mobile = request.POST.get("mobile")
        image = request.FILES.get("image")
        print(rollno, name)

    student = Student.objects.get(pk=id)

    if image:
        student.image = image
        student.save()

    student.rollno = rollno
    student.name = name
    student.age = age
    student.mobile = mobile
    student.save()
    return redirect("/student/")


def student_delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect("/student/")
