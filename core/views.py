from django.contrib import messages
from django.shortcuts import render, redirect
from .models import LoginCredential


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        try:
            user = LoginCredential.objects.get(email=email)

            if not user.check_password(password):
                messages.error(request, "Invalid email or password.")
                return redirect("core:login")

            if user.role != role:
                messages.error(request, f"Please log in as {user.role.capitalize()}, not {role.capitalize()}.")
                return redirect("core:login")

            request.session["user_id"] = user.id
            request.session["email"] = user.email
            request.session["role"] = user.role

            return redirect("home:dashboard")

        except LoginCredential.DoesNotExist:
            messages.error(request, "Invalid email or password.")

    return render(request, "core/login.html")

def signin_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("core:signin")

        if LoginCredential.objects.filter(email=email).exists():
            messages.error(request, "Account with this email already exists. Please log in.")
            return redirect("core:login")

        user = LoginCredential.objects.create(
            email=email,
            password=password,  # will be hashed in model's save()
            role=role
        )

        # Auto login after signup
        request.session["user_id"] = user.id
        request.session["email"] = user.email
        request.session["role"] = user.role

        return redirect("home:dashboard")

    return render(request, "core/signin.html")

def logout_view(request):
    request.session.flush()
    return redirect('home:home_page')
