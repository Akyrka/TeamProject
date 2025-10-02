from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("electronic_diary.urls", "electronic_diary"), namespace="electronic_diary")),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("forum/", include(("forum.urls", "forum"), namespace="forum")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)