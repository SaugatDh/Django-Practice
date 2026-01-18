from django.urls import path

from . import views
urlpatterns = [
    # path('login/',views.sign_in,name='login'),
    path('login/', views.MyLoginView.as_view(),name='login'),
    path('logout/', views.LogoutView.as_view(next_page='login'),name='logout'),
    # path('logout/',views.sign_out,name='logout'),
    # path('register/',views.sign_up,name='register'),
]
