from urllib import response
from django.shortcuts import render, redirect
from student.models import Student
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url="/student/faculty_login/")
def index(request):
    # try:
    if request.method == "POST":
        faculty = request.user.id
        rollno = request.POST.get("rollno")
        name = request.POST.get("name")
        age = request.POST.get("age")
        mobile = request.POST.get("mobile")
        image = request.FILES.get("image")

        student = Student.objects.create(
            faculty_id=faculty,
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
        name = request.POST.get("name")
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


# Login Authentication


def faculty_signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        print(name)
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already Taken")
            return redirect("/student/faculty_signup/")

        if password1 == password2:
            user = User.objects.create(first_name=name, username=username, email=email)
            user.set_password(password1)
            user.save()
            return redirect("/student/faculty_login")
        else:
            messages.error(request, "Password and confirm password are not match")
            return redirect("/student/faculty-signup/")

    return render(request, "faculty_signup.html")


def faculty_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        faculty = User.objects.filter(username=username).exists()

        if not faculty:
            messages.error(request, "Username not matching")
            return redirect("/student/faculty_login/")

        faculty = authenticate(username=username, password=password)
        print(faculty)

        if faculty is None:
            messages.error(request, "Password Incorrected")
            return redirect("/student/faculty_login/")

        else:
            login(request, faculty)
            return redirect("/student/")

    return render(request, "faculty_login.html")


def faculty_logout(request):
    logout(request)
    return redirect("/student/faculty_login/")
