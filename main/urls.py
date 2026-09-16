from django.urls import path

from main.views import show_main, show_experience, show_skills, create_project

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skills/", show_skills, name="show_skills"),
    path("projects/add/", create_project, name="create_project"),
]