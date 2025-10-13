from django import forms
from electronic_diary import models
from datetime import datetime, timedelta

TIME_CHOICES_START = [
    ("07:45", "07:45 #1"),
    ("08:30", "08:30 #2"),
    ("09:20", "09:20 #3"),
    ("10:10", "10:10 #4"),
    ("11:00", "11:00 #5"),
    ("11:50", "11:50 #6"),
    ("12:40", "12:40 #7"),
    ("13:30", "13:30 #8"),
    ("14:20", "14:20 #9"),
]

NUMBER_CHOICES = [(i, str(i)) for i in range(1, 10)]


class ScheduleForm(forms.ModelForm):
    start_time = forms.ChoiceField(choices=TIME_CHOICES_START)
    lesson_number = forms.ChoiceField(choices=NUMBER_CHOICES)
    day_of_week = forms.ChoiceField(
        choices=models.Schedule.DAYS_OF_WEEK
    )

    class Meta:
        model = models.Schedule
        fields = ['school_class', 'subject', 'teacher', 'day_of_week', 'lesson_number', 'start_time']


class CreateDiaryForm(forms.ModelForm):
    class Meta:
        model = models.DiaryEntry
        fields = ["school_class","subject","teacher","homework","due_date"]
        widgets ={"due_date": forms.DateInput(attrs={"type":"date"})}
