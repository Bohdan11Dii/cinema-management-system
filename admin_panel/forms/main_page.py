from django import forms

from admin_panel.models import MainPage


class MainPageForm(forms.ModelForm):
    class Meta:
        model = MainPage
        fields = "__all__"

