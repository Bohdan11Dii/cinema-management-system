from django.urls import reverse_lazy
from django.views import generic

from admin_panel.forms.seo import SeoForm
from admin_panel.models import SeoBlock


class SeoBlockListView(generic.ListView):
    model = SeoBlock
    template_name = "seo/seo_list.html"
    context_object_name = "seo_list"


class SeoBlockCreateView(generic.CreateView):
    model = SeoBlock
    template_name = "seo/seo_form.html"
    form_class = SeoForm
    success_url = reverse_lazy("admin_panel:seo_block_list")


class SeoBlockUpdateView(generic.UpdateView):
    model = SeoBlock
    form_class = SeoForm
    template_name = "seo/seo_form.html"
    success_url = reverse_lazy("admin_panel:seo_block_list")

class SeoBlockDeleteView(generic.DeleteView):
    model = SeoBlock
    template_name = "seo/seo_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:seo_block_list")

