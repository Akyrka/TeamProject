from django.urls import path
from . import views

app_name = "forum"

urlpatterns = [
    path("", views.ThreadListView.as_view(), name="thread_list"),
    path("<int:pk>/", views.ThreadDetailView.as_view(), name="thread_detail"),
    path("create/", views.ThreadCreateView.as_view(), name="thread_create"),
    path("<int:pk>/update/", views.ThreadUpdateView.as_view(), name="thread_update"),
    path("<int:pk>/delete/", views.ThreadDeleteView.as_view(), name="thread_delete"),
    ]