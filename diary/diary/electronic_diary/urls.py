from django.contrib import admin
from django.urls import path, include
from electronic_diary import views  
from django.contrib.auth import views as auth_views


app_name = "electronic_diary"

urlpatterns = [
    path('', views.DiaryHomeView.as_view(), name="home"),
    path('diary/', views.DiaryListView.as_view(), name="diary"),  # список всех заданий класса
    path('diary_create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary/<int:pk>/edit/', views.DiaryUpdateView.as_view(), name="diary_edit"),
]