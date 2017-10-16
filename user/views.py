from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from user.forms import RegistrationForm, LoginForm


def register(request):
    if request.user.is_authenticated:
        return redirect("main:game")
    if request.method == 'POST':

        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            first_name, last_name = user_form.cleaned_data['full_name']
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            return redirect("user:login")

    else:
        user_form = RegistrationForm()

    return render(request, "registration/register.html", {'form': user_form})


def loginView(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        email = login_form.data['email']
        password = login_form.data['password']
        if login_form.is_valid():
            user = authenticate(request, username=None, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("main:game")
    else:
        login_form = LoginForm()
    return render(request, "registration/login.html", {'form': login_form})
