from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('budget.auth_app.urls')),
    path('', include('budget.main.urls')),
]
