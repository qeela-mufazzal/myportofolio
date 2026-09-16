from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Skill
from main.forms import ProjectForm


def show_main(request):
    context = {
        "name": "Qeela Mufazzal Rafif",
        "npm": "2506637104",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Hello, whoever sees this. My name is Qeela Mufazzal Rafif, but my friends call me Qeela. I am currently (definitely not struggling) in third semester of Computer Science International Class of Universitas Indonesia"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Qeela",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skills(request):
    context = {
        'name': 'Qeela',
        'skills_list': Skill.objects.all(),
    }
    
    return render(request, 'skills.html', context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "projects_form.html", context)