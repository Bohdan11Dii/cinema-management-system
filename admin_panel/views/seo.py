from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from admin_panel.forms.seo import SeoForm
from admin_panel.models import SeoBlock
from django.contrib.messages.views import SuccessMessageMixin


class SeoBlockListView(generic.ListView):
    model = SeoBlock
    template_name = "seo/seo_list.html"
    context_object_name = "seo_list"


class SeoBlockCreateView(generic.CreateView):
    model = SeoBlock
    template_name = "seo/seo_form.html"
    form_class = SeoForm
    success_url = reverse_lazy("admin_panel:seo_block_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "SEO блок успішно створено!")
        return response


class SeoBlockUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = SeoBlock
    form_class = SeoForm
    template_name = "seo/seo_form.html"
    success_url = reverse_lazy("admin_panel:seo_block_list")
    success_message = "The main page has been updated successfully"


class SeoBlockDeleteView(generic.DeleteView):
    model = SeoBlock
    template_name = "seo/seo_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:seo_block_list")
