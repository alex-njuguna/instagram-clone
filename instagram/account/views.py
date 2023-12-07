from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .forms import SignUpForm, SignInForm


def signup(request):
    """allow for user registration"""
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created successfully for {username}!")
            return redirect("post:index")
        else:
            messages.error(request, "Error creating account. Please check the form.")

    else:
        form = SignUpForm()

    return render(request, "signup.html", {
        "form": form,
    })




