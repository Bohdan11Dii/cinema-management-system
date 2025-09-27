from django.urls import reverse_lazy
from django.views import generic

from admin_panel.forms.seance import SeanceForm
from admin_panel.models import Seance


class SeanceListView(generic.ListView):
    model = Seance
    template_name = "seance/seance_list.html"


class SeanceCreateView(generic.CreateView):
    model = Seance
    template_name = "seance/seance_form.html"
    success_url = reverse_lazy("admin_panel:seance-list")
    form_class = SeanceForm


class SeanceUpdateView(generic.UpdateView):
    model = Seance
    template_name = "seance/seance_form.html"
    success_url = reverse_lazy("admin_panel:seance-list")
    form_class = SeanceForm

    def get_queryset(self):
        return (
            Seance.objects
            .select_related("hall", "film")  # JOIN для FK
        )


class SeanceDeleteView(generic.DeleteView):
    model = Seance
    template_name = "seance/seance_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:seance-list")
