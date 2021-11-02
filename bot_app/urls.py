from django.urls import path
from . import views
import os

app_name = "bot_app"
urlpatterns= [
    path("", views.index, name="index"),
    # path(f"{os.environ['TOKEN']}", views.index, name="index"),
]