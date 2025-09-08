from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                if user.groups.filter(name='super_admin').exists():
                    return redirect('dashboard')
                elif user.groups.filter(name='agent').exists():
                    return redirect('agent')
                else:
                    return redirect('client')
            else:

                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {'form': form})

from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "dashboard/dashboard.html")


    

