from django.shortcuts import render

from main.models import Experience


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