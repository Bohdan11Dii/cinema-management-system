from django import forms

from admin_panel.models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = (
            "title",
            "description",
            "film_image",
            "link",
            "type_show",
            "seo_film",
            "format_type",

        )
