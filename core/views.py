from django.shortcuts import render, redirect
from .forms import LoginForm 

def login_view(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')   # here dashboard is the name of a url in urlpattern

    else:
        
        form = LoginForm()

    

    return render(request, 'core/login.html', {'form': form})

def login_success_view(request):
    return render(request, 'core/login_success.html')

