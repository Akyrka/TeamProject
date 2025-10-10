from django.urls import path
from .views import CalendarView, EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView

app_name = "events"

urlpatterns = [
    path("calendar/", CalendarView.as_view(), name="calendar"),
    path("", EventListView.as_view(), name="event_list"),
    path("<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("create/", EventCreateView.as_view(), name="event_create"),
    path("<int:pk>/update/", EventUpdateView.as_view(), name="event_update"),
    path("<int:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),
]