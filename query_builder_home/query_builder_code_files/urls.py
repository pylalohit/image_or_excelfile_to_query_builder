from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home' ),
    path('Create_Table',views.Create_Table, name = 'Create_Table'),
    path('instructions',views.instructions, name = 'instructions'),
    path('home',views.home, name = 'home')
]

