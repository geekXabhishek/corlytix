from django.shortcuts import render, redirect

# Create your views here.
def home_page(request):
    return render(request, "home/home_page.html")

def dashboard(request):
    if "user_id" not in request.session:
        return redirect("core:login")
    return render(request, "home/dashboard.html")