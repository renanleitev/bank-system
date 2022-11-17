from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:signin")
        else:
            return redirect("accounts/sign_in.html")
    else:
        form = UserCreationForm()
    return render(request, "accounts/create_account.html", {"form": form})

def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profiles:account_status")
        else:
            return redirect("accounts/sign_in.html")
    else:
        form = AuthenticationForm()
        return render(request, "accounts/sign_in.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("accounts:signin")
