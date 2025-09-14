from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from admin_panel.models import ContactPage
from admin_panel.forms.contact import ContactPageForm, ContactFormSet


class ContactPageListView(generic.ListView):
    model = ContactPage
    context_object_name = "contact_list"
    template_name = "contact/contact_page_list.html"


class ContactPageCreateView(generic.CreateView):
    model = ContactPage
    form_class = ContactPageForm
    template_name = "contact/contact_page_form.html"
    success_url = reverse_lazy("admin_panel:contact_page_list")

    def dispatch(self, request, *args, **kwargs):
        if ContactPage.objects.exists():
            messages.warning(request, "The contact page has already been created. Creating a new one is prohibited.")
            return redirect('admin_panel:contact_page_list')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['contact_formset'] = ContactFormSet(self.request.POST, self.request.FILES, prefix='contacts')
        else:
            context['contact_formset'] = ContactFormSet(prefix='contacts')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        contact_formset = context['contact_formset']
        if contact_formset.is_valid():
            self.object = form.save()
            contact_formset.instance = self.object
            contact_formset.save()
            return super().form_valid(form)
        return self.form_invalid(form)


class ContactPageUpdateView(generic.UpdateView):
    model = ContactPage
    form_class = ContactPageForm
    template_name = "contact/contact_page_form.html"
    success_url = reverse_lazy("admin_panel:contact_page_list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['contact_formset'] = ContactFormSet(
                self.request.POST,
                self.request.FILES,
                instance=self.object,
                prefix='contacts'
            )
        else:
            data['contact_formset'] = ContactFormSet(instance=self.object, prefix='contacts')
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        contact_formset = context['contact_formset']

        if contact_formset.is_valid():
            self.object = form.save()
            contact_formset.instance = self.object
            contact_formset.save()  # тут Django видалить ті, де DELETE=True
            return super().form_valid(form)
        return self.form_invalid(form)


class ContactPageDeleteView(generic.DeleteView):
    model = ContactPage
    context_object_name = "contact_page"
    template_name = "contact/contact_page_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:contact_page_list")
