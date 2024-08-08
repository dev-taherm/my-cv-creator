from django import forms

from portfolio.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "bio",
            "template_choice",
        ]
