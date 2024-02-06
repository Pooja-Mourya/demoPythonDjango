from django.urls import path

from index.views import *

urlpatterns = [
    path("", index, name="index"),
]