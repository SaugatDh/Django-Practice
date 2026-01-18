from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate,login,logout
# Create your views here.


# def sign_in(request):
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             return redirect('posts')
        
#         form = LoginForm()
#         return render(request, 'login.html', {'form': form})
#     elif request.method == 'POST':
#         form = LoginForm(request.POST)
        
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user = authenticate(request,username=username,password=password)
#             if user:
#                 login(request, user)
#                 messages.success(request,f'Hi {username.title()}, welcome back!')
#                 return redirect('posts')

#     messages.error(request,f'Invalid username or password')
#     return render(request,'login.html',{'form':form})

# def sign_out(request):
#     logout(request)
#     messages.success(request,f'You have been logged out.')
#     return redirect('login')

# def sign_up(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#         return render(request,'register.html',{'form':form})
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             messages.success(request,'You have signed up successfully.')
#             login(request,user)
#             return redirect('posts')
#         else:
#             return render(request,'register.html',{'form':form})

class MyLoginView(LoginView):
    redirect_authenticated_user=True
    
    def get_success_url(self):
        return reverse_lazy('posts')
    
    def form_invalid(self,form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    