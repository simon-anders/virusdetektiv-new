
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('token', views.token),
    path('order', views.order),
    path('admin/', admin.site.urls),
]
