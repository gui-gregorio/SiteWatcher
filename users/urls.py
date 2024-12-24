from django.urls import path
from .views import register_user, list_user


urlpatterns = [
    path("register_user", register_user, name="register_user"),
    path("list_user", list_user, name="list_user"),
]