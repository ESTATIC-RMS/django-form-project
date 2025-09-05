from django.contrib import admin
from django.urls import path
from userauths import views

urlpatterns = [
    path('',views.home,name="home"),
    path('candidates/<int:id>',views.candidate_details,name="candidate"),
    
]