from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin



# from .forms import RegisterForm
# Create your views here.
class UserSignupView(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("signup")

        user = CustomUser(email=email, phone=phone)
        user.set_password(password)
        user.save()
        
        messages.success(request, "Account created successfully")
        return redirect("login")

class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            full_name = user.get_full_name()
            welcome_message = f"Welcome back, {full_name}!" if full_name.strip() else f"Welcome back, {user.email}!"
            messages.success(request, welcome_message)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')
        
class UserLogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect('login')

