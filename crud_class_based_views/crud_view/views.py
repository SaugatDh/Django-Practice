from django.shortcuts import redirect, render
from crud_view.models import Product
from django.views.generic import View
from django.contrib import messages
from django.db import transaction

# Create your views here.
class ProductView(View):
    template_name = 'index.html'
    
    def get(self,request):
        products = Product.objects.all()
        context = {
            'products':products,
        }
        return render(request,self.template_name,context)
    
    def post(self,request):
        action = request.POST.get('action')
        id = request.POST.get('id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        try:
            with transaction.atomic():
                if action == "create":
                    Product.objects.create(name=name,description=description,price=price,stock = stock)
                    messages.success(request,'Product created successfully.')
                    
                elif action == "delete":
                    product = Product.objects.get(id=id)
                    product.delete()
                    messages.success(request,'Product updated Successfully.')
                else:
                    messages.error(request,'Invalid Action.')
        except Exception as e:
            messages.error(request,f"Error:{e}")
        return redirect('prouct-list')