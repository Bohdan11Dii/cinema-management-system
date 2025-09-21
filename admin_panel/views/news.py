from django.urls import reverse_lazy
from django.views import generic

from admin_panel.forms.image import GalleryImageFormSet
from admin_panel.forms.news import NewsForm
from admin_panel.mixin import FormsetMixin
from admin_panel.models import News


class NewsListView(generic.ListView):
    model = News
    template_name = "news/news_list.html"


class NewsCreateView(FormsetMixin, generic.CreateView):
    model = News
    form_class = NewsForm
    template_name = "news/news_form.html"
    success_url = reverse_lazy("admin_panel:news-list")
    formset_class = GalleryImageFormSet


class NewsUpdateView(FormsetMixin, generic.UpdateView):
    model = News
    form_class = NewsForm
    template_name = "news/news_form.html"
    success_url = reverse_lazy("admin_panel:news-list")
    formset_class = GalleryImageFormSet


class NewsDeleteView(generic.DeleteView):
    model = News
    template_name = "news/news_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:news-list")
