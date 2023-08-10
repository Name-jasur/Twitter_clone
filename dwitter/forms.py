from django import forms
from .models import Dweet, Profile



class UserForm(forms.ModelForm):
    class Meta:
        moedel = Profile
        fields = ('image', 'user')


class DweetFrom(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Dweet
        exclude = ("user", )
