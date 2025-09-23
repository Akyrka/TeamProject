from django.urls import path
from .views import RegisterView, CustomLoginView, UserLogoutView, ProfileView, ProfileEditView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path("profile/", ProfileView.as_view(),name="profile"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
]
