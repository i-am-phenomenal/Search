from django.contrib import admin
from django.urls import path
from backendApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.returnSimpleResponse)
]
