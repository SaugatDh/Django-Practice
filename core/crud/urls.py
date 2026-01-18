from django.urls import path
from . import views

urlpatterns = [
    # path('crud/',views.crud,name='crud'),
    path('create/', views.create_item, name='create_item'),
    path('delete/<int:id>',views.delete_item,name='delete_item'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
]