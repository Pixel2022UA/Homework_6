from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TeacherForm, GroupForm
from .models import Teacher, Group

from faker import Faker

fake = Faker()


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/teachers/")
    else:
        initial_data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "date_of_birthday": fake.date_of_birth().strftime("%Y-%m-%d"),
            "subject": fake.random_element(
                elements=("Math", "Science", "History", "Biology", "Music")
            ),
        }
        form = TeacherForm(initial=initial_data)
    return render(request, "teacher.html", {"form": form})


def get_teacher_data(request):
    teachers = Teacher.objects.all()
    teachers_data = {"teachers": teachers}
    return render(request, "teachers_list.html", context=teachers_data)


def add_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/groups/")
    else:
        form = GroupForm()
    return render(request, "group.html", {"form": form})


def get_group_data(request):
    groups = Group.objects.all()
    groups_data = {"groups": groups}
    return render(request, "groups_list.html", context=groups_data)
