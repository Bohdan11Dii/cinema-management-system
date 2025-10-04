from django.urls import reverse_lazy
from django.views import generic

from admin_panel.forms.ciname_hall import CinemaForm
from admin_panel.forms.image import GalleryImageFormSet
from admin_panel.mixin import FormsetMixin
from admin_panel.models import Cinema


class CinemaListView(generic.ListView):
    model = Cinema
    template_name = "cinema_hall/cinema/cinema_list.html"
    paginate_by = 5

class CinemaCreateView(FormsetMixin, generic.CreateView):
    model = Cinema
    template_name = "cinema_hall/cinema/cinema_form.html"
    success_url = reverse_lazy("admin_panel:cinema-list")
    form_class = CinemaForm
    formset_class = GalleryImageFormSet


class CinemaUpdateView(FormsetMixin, generic.UpdateView):
    model = Cinema
    template_name = "cinema_hall/cinema/cinema_form.html"
    success_url = reverse_lazy("admin_panel:cinema-list")
    form_class = CinemaForm
    formset_class = GalleryImageFormSet

    def get_queryset(self):
        return (
            Cinema.objects
            .select_related("collection", "seo_cinema")  # JOIN для FK
            .prefetch_related("collection__images")  # всі картинки з колекції
        )


class CinemaDeleteView(generic.DeleteView):
    model = Cinema
    template_name = "cinema_hall/cinema/cinema_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:cinema-list")


# Crete CRUD for Hall
