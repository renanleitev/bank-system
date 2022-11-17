from django.urls import include, re_path
from . import views

app_name = "accounts"

urlpatterns = [
    re_path("register/", views.register, name = "signup"),
    re_path("login/", views.sign_in, name = "signin"),
    re_path("logout/", views.logout_view, name = "logout"),
]
