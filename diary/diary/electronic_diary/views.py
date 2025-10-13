from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from electronic_diary import models
from electronic_diary.forms import CreateDiaryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View, TemplateView
from django.http import HttpResponseForbidden
# Create your views here.

class DiaryHomeView(ListView):
    model=models.DiaryEntry
    template_name="electronic_diary/home.html"




class DiaryDetailView(LoginRequiredMixin, DetailView):
    model = models.DiaryEntry
    template_name = "electronic_diary/diary.html"


class DiaryListView(LoginRequiredMixin, ListView):  
    model = models.DiaryEntry
    template_name = "electronic_diary/diary.html"


    def get_queryset(self):
        user = self.request.user

        # Если это учитель — показываем все записи с возможностью фильтра по классу
        if hasattr(user, "teacher"):
            school_class_id = self.request.GET.get("class_id")
            if school_class_id:
                return models.DiaryEntry.objects.filter(school_class_id=school_class_id)
            return models.DiaryEntry.objects.all()

        # Если это ученик — только его класс
        profile = getattr(user, "profile", None)
        if profile and profile.school_class:
            return models.DiaryEntry.objects.filter(school_class=profile.school_class)

        return models.DiaryEntry.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self.request.user, "teacher"):
            context["school_classes"] = models.SchoolClass.objects.all()
        return context




class DiaryCreateView(LoginRequiredMixin,CreateView):
    model=models.DiaryEntry
    form_class = CreateDiaryForm
    template_name="electronic_diary/diary_create.html"
    success_url = reverse_lazy("electronic_diary:diary")
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, "teacher"):
            return HttpResponseForbidden("Тільки вчителі можуть створювати завдання")
        return super().dispatch(request, *args, **kwargs)

class DiaryUpdateView(LoginRequiredMixin,UpdateView):
    model = models.DiaryEntry
    form_class = CreateDiaryForm
    template_name="electronic_diary/diary_edit.html"
    success_url = reverse_lazy("electronic_diary:diary")