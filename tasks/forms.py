from django.utils import timezone

from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags",]

        widgets = {
            "deadline": forms.DateInput(
                attrs={
                    "type": "date",
                    "min": timezone.now().date()
                }
            ),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
