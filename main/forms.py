from django.forms import ModelForm, TextInput, Textarea
from main.models import Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
        ]

        labels = {
            "title": "Experience Name",
            "description": "Description",
            "category": "Experience Type",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your project",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
        }