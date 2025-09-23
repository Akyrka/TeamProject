from django.shortcuts import render
from django.urls import reverse_lazy
from electronic_diary import models
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View, TemplateView

# Create your views here.

class DiaryListView(ListView):
    model=models.DiaryEntry
    template_name="electronic_diary/home.html"