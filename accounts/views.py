from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, 'accountsIndex.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login_url')

    return render(request, 'registration/register.html')
