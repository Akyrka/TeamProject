from django import forms
from .models import ForumThread, ForumPost
class ForumThreadForm(forms.ModelForm):
    class Meta:
        model = ForumThread
        fields = ["title", "description"]

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ["text"]