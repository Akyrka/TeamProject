from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm
import calendar
from datetime import date

class CalendarView(TemplateView):
    template_name = "events/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        year = int(self.request.Get.get("year", today.year))
        month = int(self.request.Get.get("month", today.month))

        cal = calendar.Calendar()
        month_days = cal.itermonthdays(year, month)
        events = Event.objects.filter(start_time__year=year, start_time__month=month)
        day_events = {}
        for event in events:
            day = event.start_time.day
            day_events.setdefault(day, []).append(event)
            context.update({
                "year": year,
                "month": month,
                "month_days": month_days,
                "day_events": day_events,
            })
        return context


class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"
    ordering = ["-updated_at"]
    paginate_by = 10

class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"



class EventCreateView(UserPassesTestMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "events/event_form.html"
    success_url = reverse_lazy("forum:thread_list")

    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.author = self.request.user
        thread.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class EventUpdateView(UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "events/event_form.html"

    def get_success_url(self):
        return reverse_lazy("events/event_detail.html", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class EventDeleteView(UserPassesTestMixin, DeleteView):
    model = Event
    template_name = "events/event_confirm_delete.html"
    success_url = reverse_lazy("events/event_list.html")

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser
