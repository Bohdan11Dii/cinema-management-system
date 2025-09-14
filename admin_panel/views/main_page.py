from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from admin_panel.models import MainPage
from admin_panel.forms.main_page import MainPageForm

class MainPageListView(generic.ListView):
    model = MainPage
    context_object_name = 'main_page_list'
    template_name = "main/main_page_list.html"

class MainPageCreateView(generic.CreateView):
    model = MainPage
    form_class = MainPageForm
    template_name = "main/main_page_form.html"
    success_url = reverse_lazy("admin_panel:main_page_list")


    def dispatch(self, request, *args, **kwargs):
        # Якщо вже є хоча б один MainPage – редіректимо на список
        if MainPage.objects.exists():
            messages.warning(request, "Головна сторінка вже створена. Створення нової заборонено.")
            return redirect('admin_panel:main_page_list')
        return super().dispatch(request, *args, **kwargs)

class MainPageUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = MainPage
    form_class = MainPageForm
    template_name = "main/main_page_form.html"
    success_url = reverse_lazy("admin_panel:main_page_list")
    success_message = "The main page has been updated successfully"

class MainPageDeleteView(generic.DeleteView):
    model = MainPage
    template_name = "main/main_page_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:main_page_list")
