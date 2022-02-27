from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView
app_name = "promApp"
urlpatterns = [

    path("", views.index, name="index"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("about", views.about, name="about"),
    path("app", views.app, name="app"),
    path("sorry", views.sorry, name="sorry")

]