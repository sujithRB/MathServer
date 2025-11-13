from django.contrib import admin
from django.urls import path
from bulb import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.powerlamp,name="powerlamp"),]