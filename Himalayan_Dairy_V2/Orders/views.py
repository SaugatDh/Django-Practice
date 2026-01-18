from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MilkOrder




class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Logic to separate Staff view from Customer view
        if self.request.user.is_staff_user:
            context['orders'] = MilkOrder.objects.all().order_by('-order_at')
        else:
            context['my_orders'] = MilkOrder.objects.filter(user=self.request.user).order_by('-order_at')
        
        return context

    def post(self, request, *args, **kwargs):
        # Prevent staff from placing orders through this logic if needed
        if not request.user.is_staff_user:
            milk_type = request.POST.get('milk_type')
            quantity = request.POST.get('quantity')

            if milk_type and quantity:
                MilkOrder.objects.create(
                    user=request.user,
                    milk_type=milk_type,
                    quantity=quantity
                )
                messages.success(request, "Order placed successfully!")
            else:
                messages.error(request, "Please provide both milk type and quantity.")
        
        return redirect('home')