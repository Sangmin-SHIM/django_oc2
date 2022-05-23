from django.contrib import admin
from django.urls import path

from authentication import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication_views.login_page, name="login"),
]
