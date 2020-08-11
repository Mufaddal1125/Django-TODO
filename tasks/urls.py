from django.urls import path
from . import views
urlpatterns = [
     path("", views.index, name="index"),
     path("add", views.add, name="add"),
     path("removetask/", views.removetask, name="removetask"),
     path("incpriority/<int:index>", views.inc, name="inc"),
     path("decpriority/<int:index>", views.dec, name="dec"),
]