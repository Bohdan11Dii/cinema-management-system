from django import forms

from admin_panel.models import Cinema, Hall


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = (
            "title",
            "description",
            "condition",
            "logo_cinema",
            "banner_cinema",
            "seo_cinema",
        )


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = (
            "title",
            "description",
            "logo_hall",
            "banner_hall",
            "seo_hall",
            "cinema"
        )
