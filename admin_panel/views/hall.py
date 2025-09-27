from django.urls import reverse_lazy
from django.views import generic

from admin_panel.forms.ciname_hall import HallForm
from admin_panel.forms.image import GalleryImageFormSet
from admin_panel.mixin import FormsetMixin
from admin_panel.models import Hall


class HallListView(generic.ListView):
    model = Hall
    template_name = "cinema_hall/hall/hall_list.html"


class HallCreateView(FormsetMixin, generic.CreateView):
    model = Hall
    template_name = "cinema_hall/hall/hall_form.html"
    success_url = reverse_lazy("admin_panel:hall-list")
    form_class = HallForm
    formset_class = GalleryImageFormSet


class HallUpdateView(FormsetMixin, generic.UpdateView):
    model = Hall
    template_name = "cinema_hall/hall/hall_form.html"
    success_url = reverse_lazy("admin_panel:hall-list")
    form_class = HallForm
    formset_class = GalleryImageFormSet

    def get_queryset(self):
        return (
            Hall.objects
            .select_related("collection", "seo_hall", "cinema")  # JOIN для FK
            .prefetch_related("collection__images")  # всі картинки з колекції
        )


class HallDeleteView(generic.DeleteView):
    model = Hall
    template_name = "cinema_hall/hall/hall_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:hall-list")
