from django.contrib import admin
from django.urls import path, include
from electronic_diary import views  
from django.contrib.auth import views as auth_views


app_name = "electronic_diary"

urlpatterns = [
    path('', views.DiaryHomeView.as_view(), name="home"),
    path('diary/', views.DiaryListView.as_view(), name="diary"), 
    path('diary_create/', views.DiaryCreateView.as_view(), name="diary-create"),
    path('diary/<int:pk>/edit/', views.DiaryUpdateView.as_view(), name="diary-edit"),
    path("<int:pk>/delete/", views.DiaryDeleteView.as_view(), name="homework-delete"),
    path("schedule/", views.ScheduleListView.as_view(), name="schedule"),
    path("schedule_create/", views.ScheduleCreateView.as_view(), name="schedule-create"),
    path('schedule/<int:pk>/delete/', views.ScheduleDeleteView.as_view(), name='schedule-delete'),


]