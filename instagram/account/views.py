from django.shortcuts import render
from django.contrib import messages

from .forms import SignUpForm


def signup(request):
    """allow for user registration"""
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            messages.success(request, f"Account created successfully for {email}!")
            return redirect("home")  # Replace "home" with the URL or name of the view where you want to redirect after successful registration
        else:
            messages.error(request, "Error creating account. Please check the form.")

    else:
        form = SignUpForm()

    return render(request, "signup.html", {
        "form": form,
    })



