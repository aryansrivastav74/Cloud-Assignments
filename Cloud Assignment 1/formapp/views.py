from django.shortcuts import render, redirect
from .forms import UserDataForm
import hashlib

def home(request):
    if request.method == "POST":
        form = UserDataForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = hashlib.sha256(user.password.encode()).hexdigest()
            user.save()
            return redirect('success')
    else:
        form = UserDataForm()

    return render(request, "home.html", {"form": form})

def success(request):
    return render(request, "success.html")
