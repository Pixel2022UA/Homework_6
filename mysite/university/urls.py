from django.urls import path

from . import views

urlpatterns = [
    path("teacher/", views.add_teacher, name="teacher"),
    path("teachers/", views.get_teacher_data, name="teachers"),
    path("group/", views.add_group, name="group"),
    path("groups/", views.get_group_data, name="groups"),
]
