from crispy_forms.helper import FormHelper
from django import forms
from admin_panel.models import BackgroundBanner, Banner
from crispy_forms.layout import Layout, Field, Submit

class BackgroundBannerForm(forms.ModelForm):
    class Meta:
        model = BackgroundBanner
        fields = "__all__"


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = (
            "type",
            "is_published",
            "rotation_speed",
        )

        widgets = {
            'type': forms.Select(attrs={'class': 'form-select form-select-lg mb-3"'}),
        }
