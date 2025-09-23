from django.contrib import admin
from django.urls import path, include
from electronic_diary import views  
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.DiaryListView.as_view(), name="home")
]