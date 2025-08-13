
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('book.urls')),  # your app's urls
  # ✅ Add built-in auth routes (login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
]

