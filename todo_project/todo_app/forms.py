from django import forms
from .models import Task


# Create your forms here.

class todoform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'Date']
