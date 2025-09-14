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