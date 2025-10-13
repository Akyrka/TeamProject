from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.views.generic import FormView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, ProfileEditForm
from accounts import models

# Регистрация пользователя
class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("electronic_diary:home")  # <-- имя маршрута главной страницы

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # сразу авторизация
        return super().form_valid(form)


# Логин пользователя
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy("electronic_diary:home")


# Логаут пользователя
class UserLogoutView(LogoutView):
    # Здесь тоже нужен namespace
    next_page = reverse_lazy("accounts:login")


# Профиль пользователя
class ProfileView(LoginRequiredMixin, DetailView):
    model = models.Profile
    template_name = "accounts/profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return self.request.user.profile


# Редактирование профиля
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = models.Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')  

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        return self.request.user.profile
