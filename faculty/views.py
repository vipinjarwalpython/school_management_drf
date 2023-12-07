from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

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
            return redirect("/faculty/faculty_signup/")

        if password1 == password2:
            user = User.objects.create(first_name=name, username=username, email=email)
            user.set_password(password1)
            user.save()
            return redirect("/faculty/faculty_login")
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
            return redirect("/faculty/faculty_login/")

        faculty = authenticate(username=username, password=password)
        print(faculty)

        if faculty is None:
            messages.error(request, "Password Incorrected")
            return redirect("/faculty/faculty_login/")

        else:
            login(request, faculty)
            return redirect("/student/")

    return render(request, "faculty_login.html")


def faculty_logout(request):
    logout(request)
    return redirect("/faculty/faculty_login/")
