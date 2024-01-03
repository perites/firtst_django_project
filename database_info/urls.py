from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_db_info)
]