from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "start_time", "end_time", "status"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Введіть назву події"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control form-control-sm",
                "rows": 3,
                "placeholder": "Короткий опис події..."
            }),
            "start_time": forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "class": "form-control form-control-sm"
            }),
            "end_time": forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "class": "form-control form-control-sm"
            }),
            "status": forms.Select(attrs={
                "class": "form-select form-select-sm"
            }),
        }