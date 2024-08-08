from django import forms
from experience.models import Experience


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "company",
            "description",
            "start_date",
            "end_date",
        ]
