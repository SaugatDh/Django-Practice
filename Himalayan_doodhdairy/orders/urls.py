from django.urls import path
from . import views

urlpatterns = [
    # path('orders/', views.staff_orders, name='staff_orders'),
    path('home/', views.home_view, name='home'),

]
