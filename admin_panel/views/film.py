from django.urls import reverse_lazy
from django.views import generic

from admin_panel.forms.film import FilmForm
from admin_panel.forms.image import GalleryImageFormSet
from admin_panel.mixin import FormsetMixin
from admin_panel.models import Film


class FilmListView(generic.ListView):
    model = Film
    template_name = "film/film_list.html"

class FilmCreateView(FormsetMixin,generic.CreateView):
    model = Film
    template_name = "film/film_form.html"
    success_url = reverse_lazy("admin_panel:film-list")
    form_class = FilmForm
    formset_class = GalleryImageFormSet

class FilmDetailView(generic.DetailView):
    model = Film
    template_name = "film/film_detail.html"


class FilmUpdateView(FormsetMixin,generic.UpdateView):
    model = Film
    template_name = "film/film_form.html"
    success_url = reverse_lazy("admin_panel:film-list")
    form_class = FilmForm
    formset_class = GalleryImageFormSet

class FilmDeleteView(generic.DeleteView):
    model = Film
    template_name = "film/film_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:film-list")
