from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('aye.urls')),
    path('', include('aye.urls')),

]