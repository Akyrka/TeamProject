from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ForumThread, ForumPost
from .forms import ForumThreadForm, ForumPostForm


class ThreadListView(ListView):
    model = ForumThread
    template_name = "forum/thread_list.html"
    context_object_name = "threads"
    ordering = ["-updated_at"]
    paginate_by = 10


class ThreadDetailView(DetailView):
    model = ForumThread
    template_name = "forum/thread_detail.html"
    context_object_name = "thread"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = self.object.posts.all().order_by("created_at")
        context["form"] = ForumPostForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return redirect("accounts:login")

        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.thread = self.object
            post.save()
            return redirect("forum:thread_detail", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class ThreadCreateView(UserPassesTestMixin, CreateView):
    model = ForumThread
    form_class = ForumThreadForm
    template_name = "forum/thread_form.html"
    success_url = reverse_lazy("forum:thread_list")

    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.author = self.request.user
        thread.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class ThreadUpdateView(UserPassesTestMixin, UpdateView):
    model = ForumThread
    form_class = ForumThreadForm
    template_name = "forum/thread_form.html"

    def get_success_url(self):
        return reverse_lazy("forum:thread_detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class ThreadDeleteView(UserPassesTestMixin, DeleteView):
    model = ForumThread
    template_name = "forum/thread_confirm_delete.html"
    success_url = reverse_lazy("forum:thread_list")

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser