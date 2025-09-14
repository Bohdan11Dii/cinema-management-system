from django import forms
from django.forms import modelformset_factory, inlineformset_factory

from admin_panel.models import ContactPage, Contact


class ContactForm(forms.ModelForm):
    model = Contact
    fields = ['title', 'address', 'coordinates', 'is_active', 'logo']


class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = '__all__'


ContactFormSet = inlineformset_factory(
    ContactPage,
    Contact,
    form=ContactForm,
    extra=1,
    can_delete=True,
    exclude=("page",)
)
