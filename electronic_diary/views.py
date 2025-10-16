from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from electronic_diary import models
from electronic_diary.forms import CreateDiaryForm, ScheduleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View, TemplateView
from django.http import HttpResponseForbidden
from datetime import datetime


class DiaryHomeView(ListView):
    model=models.DiaryEntry
    template_name="electronic_diary/home.html"

class ScheduleCreateView(LoginRequiredMixin,CreateView):
    model = models.Schedule
    form_class = ScheduleForm
    template_name = "electronic_diary/schedule_create.html"
    success_url = reverse_lazy("electronic_diary:schedule")

    def form_valid(self, form):
        start_time_str = form.cleaned_data['start_time']
        form.instance.start_time = datetime.strptime(start_time_str, "%H:%M").time()
        form.save()  
        return redirect(self.success_url)
    

class ScheduleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Schedule
    template_name = "electronic_diary/schedule_delete.html"
    success_url = reverse_lazy("electronic_diary:schedule")



class ScheduleListView(LoginRequiredMixin, ListView):
    model = models.Schedule
    template_name = "electronic_diary/schedule.html"
    context_object_name = "schedules"

    def get_queryset(self):
        user = self.request.user
        request = self.request
        queryset = models.Schedule.objects.order_by("day_of_week", "lesson_number")


        class_id = request.GET.get("class_id")
        if class_id:
            request.session["selected_class_id"] = class_id
        else:
            class_id = request.session.get("selected_class_id")


        if hasattr(user, "teacher"):
            if class_id:
                queryset = queryset.filter(school_class_id=class_id)
        else: 
            profile = getattr(user, "profile", None)
            if profile and profile.school_class:
                queryset = queryset.filter(school_class=profile.school_class)
            else:
                return models.Schedule.objects.none()

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grouped = {}
        for sched in context["schedules"]:
            grouped.setdefault(sched.day_of_week, []).append(sched)
        context["grouped_schedules"] = grouped

        if hasattr(self.request.user, "teacher"):
            context["school_classes"] = models.SchoolClass.objects.all()
            context["selected_class_id"] = self.request.session.get("selected_class_id")

        return context



class DiaryListView(LoginRequiredMixin, ListView):  
    model = models.DiaryEntry
    template_name = "electronic_diary/diary.html"
    context_object_name = "object_list"
    paginate_by = 10 


    def get_queryset(self):
        user = self.request.user
        request = self.request


        school_class_id = request.GET.get("class_id")
        subject_id = request.GET.get("subject")

        # Если фильтры переданы — сохраняем их в сессии
        if school_class_id:
            request.session["selected_class_id"] = school_class_id
        elif school_class_id == "":
            request.session.pop("selected_class_id", None)
        else:
            school_class_id = request.session.get("selected_class_id")

        if subject_id:
            request.session["selected_subject_id"] = subject_id
        elif subject_id == "":
            request.session.pop("selected_subject_id", None)
        else:
            subject_id = request.session.get("selected_subject_id")


        queryset = models.DiaryEntry.objects.all()

        # Фильтрация по роли
        if hasattr(user, "teacher"):
            if school_class_id:
                queryset = queryset.filter(school_class_id=school_class_id)
        else:
            profile = getattr(user, "profile", None)
            if profile and profile.school_class:
                queryset = queryset.filter(school_class=profile.school_class)
            else:
                return models.DiaryEntry.objects.none()

        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request

        if hasattr(request.user, "teacher"):
            context["school_classes"] = models.SchoolClass.objects.all()
            context["selected_class_id"] = request.session.get("selected_class_id")

        context["subjects"] = models.Subject.objects.all()
        context["selected_subject_id"] = request.session.get("selected_subject_id")

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

class DiaryDeleteView(LoginRequiredMixin,DeleteView):
    model = models.DiaryEntry
    template_name = "electronic_diary/homework_confirm_delete.html"
    success_url = reverse_lazy("electronic_diary:diary")

    