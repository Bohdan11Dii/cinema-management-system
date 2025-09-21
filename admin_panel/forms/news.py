from django import forms
from admin_panel.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "description",
            "image",
            "is_published",
            "published_date",
            "link_url",
            "seo_news",
            "type_page",
        ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'my-image-class'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'my-checkbox-input'}),
        }
        labels = {
            'is_published': '',  # ось тут лейбл
        }
