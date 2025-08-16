from django import forms
from .models import JobApplicant

class JobApplyForm(forms.ModelForm):
    class Meta:
        model = JobApplicant
        fields = ['resume']