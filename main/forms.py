from django.forms import ModelForm, TextInput, Textarea, Select
from main.models import Experience

class ExperienceForm(ModelForm):
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
            "category": "Category",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "e.g. Teaching Assistant for PBP",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your responsibilities or achievements...",
                    "rows": 3,
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }