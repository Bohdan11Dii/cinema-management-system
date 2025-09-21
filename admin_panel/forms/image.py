# Formset для мульти-картинок
from django import forms
from django.forms import inlineformset_factory

from admin_panel.models import ImageTitle, GalleryImage

GalleryImageFormSet = inlineformset_factory(
    ImageTitle,
    GalleryImage,
    fields=["image", "url", "text"],
    extra=1,
    can_delete=True,
)
