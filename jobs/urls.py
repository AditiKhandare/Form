from django.contrib import admin
from django.urls import path

from jobs import views


urlpatterns = [
        path('post/', views.EntryList.post, name="post"),
        path('get/', views.EntryList.get, name="get"),
        path('add/', views.add, name="add"),
        path('totalentrys/', views.totalentrys, name="totalentrys"),
        path('phone/', views.number),

    ]  