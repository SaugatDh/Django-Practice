from django.urls import path,include
from authentication.views import *
# from . import views
urlpatterns =[
    path('',home,name="home"),
    path('home/',home,name="home"),
    path("login/",login_page,name="login_page"),
    path("register/",register_page,name='register'),
    path('logout/', logout_page, name='logout_page'),  
] 