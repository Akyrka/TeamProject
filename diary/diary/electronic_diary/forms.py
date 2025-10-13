from django import forms
from electronic_diary import models

class CreateDiaryForm(forms.ModelForm):
    class Meta:
        model = models.DiaryEntry
        fields = ["school_class","subject","teacher","homework","due_date"]
        widgets ={"due_date": forms.DateInput(attrs={"type":"date"})}

# class ListDiaryForm(forms.ModelForm):
#     class Meta:
#         model = models.DiaryEntry