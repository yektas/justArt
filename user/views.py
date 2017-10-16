from django.shortcuts import render, redirect

from user.forms import RegistrationForm


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
