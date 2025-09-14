# admin_panel/forms/seo.py

from django import forms
from admin_panel.models.seo import SeoBlock

class SeoForm(forms.ModelForm):
    class Meta:
        model = SeoBlock
        fields = "__all__"

    # Додаткову логіку валідації можна прописувати тут
    def clean_url(self):
        url = self.cleaned_data.get('url')
        if not url.startswith("http"):
            raise forms.ValidationError("URL повинен починатися з http або https")
        return url
