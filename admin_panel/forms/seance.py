from django import forms

from admin_panel.models import Seance


class SeanceForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = (
            "film",
            "hall",
            "cinema",
            "format_type",
            "price",
            "datetime"
        )
