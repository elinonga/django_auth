from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("backend.authtokens.urls")),
    path("users/", include("backend.users.urls")),
]
