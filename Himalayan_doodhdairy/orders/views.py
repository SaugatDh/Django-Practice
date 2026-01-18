from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from .models import MilkOrder
# Create your views here.
# def is_staff_user(user):
#     return user.is_staff_user


# @login_required
def home_view(request):
    # --- PART 1: HANDLE POST (Customer placing order) ---
    if request.method == "POST" and not request.user.is_staff:
        milk_type = request.POST.get('milk_type')
        quantity = request.POST.get('quantity')
        
        if milk_type and quantity:
            MilkOrder.objects.create(
                user=request.user,
                milk_type=milk_type,
                quantity=quantity
            )
            messages.success(request, "Order placed successfully!")
            return redirect('home')

    context = {}
    
    if request.user.is_staff_user:
        # If user is staff or admin, get orders
        context['orders'] = MilkOrder.objects.all().order_by('-order_at')
    else:
        # If user is a customer, get ONLY their orders
        context['my_orders'] = MilkOrder.objects.filter(user=request.user).order_by('-order_at')

    return render(request, 'home.html', context)
# @login_required
# def staff_orders(request):
#     orders = MilkOrder.objects.all().order_by('order_at')
#     return render(request,'home.html',{'orders':orders})
