from django.urls import path

from . import views

urlpatterns = [
    path("users", views.users, name="users"),
    path("create", views.create, name="create"),
    path("delete", views.delete, name="delete"),
    path("match", views.match, name="match")
]