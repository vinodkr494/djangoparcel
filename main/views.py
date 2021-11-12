from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


@login_required
def home(request):
    template = "home.html"
    return render(request, template)


@login_required
def customer_page(request):
    template = "home.html"
    return render(request, template)


@login_required
def courier_page(request):
    template = "home.html"
    return render(request, template)


def sign_up(request):
    template = "sign_up.html"
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()
            user = form.save(commit=False)
            user.username = email
            user.save()

            login(request, user)
            return redirect("/")

    return render(request, template, {"form": form})
