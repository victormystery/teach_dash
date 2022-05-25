from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth import logout
from .forms import TeacherRegister

# Create your views here.
def teacher(request):
    return render(request, "dashboard.html")



def teacherlogin(request):
    
    if request.method == 'POST':
        form = TeacherRegister(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, name=name,  password=password)

            if user is not None:
                login(request, user)
                return redirect("teacher")

            else:
                messages.info(request, 'invalid credentials')
                return redirect("teacherlogin")

    else:
        form = TeacherRegister()
    return render(request, "teach-login.html")

def teachreg(request):
    form = TeacherRegister()
    if request.method == 'POST':
        form = TeacherRegister(request.POST)
        if form.is_valid():

            form.save()

            return redirect("teacherlogin")

    context = {'form': form}
    return render(request, 'dashreg.html', context)




