from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("gomoku-narabe/", include("gomokunarabe.urls")), 
    path("admin/", admin.site.urls),
]
