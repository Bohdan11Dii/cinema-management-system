from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from admin_panel.forms.banner import BackgroundBannerForm, BannerForm
from admin_panel.forms.image import GalleryImageFormSet
from admin_panel.mixin import FormsetMixin
from admin_panel.models import BackgroundBanner, Banner, ImageTitle


class BackgroundListView(generic.ListView):
    model = BackgroundBanner
    template_name = "background_banner/back_list.html"
    context_object_name = "back_list"


class BackgroundCreateView(generic.CreateView):
    model = BackgroundBanner
    form_class = BackgroundBannerForm
    template_name = "background_banner/back_form.html"
    success_url = reverse_lazy("admin_panel:back-list")

    def dispatch(self, request, *args, **kwargs):
        if BackgroundBanner.objects.exists():
            messages.warning(request,
                             "The background banner page has already been created. Creating a new one is prohibited.")
            return redirect('admin_panel:back-list')
        return super().dispatch(request, *args, **kwargs)


class BackgroundUpdateView(generic.UpdateView):
    model = BackgroundBanner
    form_class = BackgroundBannerForm
    template_name = "background_banner/back_form.html"
    success_url = reverse_lazy("admin_panel:back-list")


class BackgroundDeleteView(generic.DeleteView):
    model = BackgroundBanner
    template_name = "background_banner/back_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:back-list")


# Create CRUD for Banner
class BannerListView(generic.ListView):
    model = Banner
    template_name = "banner/banner_list.html"


class BannerCreateView(FormsetMixin, generic.CreateView):
    model = Banner
    form_class = BannerForm
    template_name = "banner/banner_form.html"
    success_url = reverse_lazy("admin_panel:banner-list")
    formset_class = GalleryImageFormSet

    # Перевірка, щоб не створювати більше одного банера
    # def dispatch(self, request, *args, **kwargs):
    #     if Banner.objects.exists():
    #         messages.warning(request,
    #                          "The banner page has already been created. Creating a new one is prohibited.")
    #         return redirect('admin_panel:banner-list')
    #     return super().dispatch(request, *args, **kwargs)

    # Переоприділення form_valid для створення collection та збереження formset
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        with transaction.atomic():
            # Зберігаємо основний об’єкт Banner
            self.object = form.save()

            # Створюємо collection, якщо його ще немає
            if not getattr(self.object, self.formset_instance_attr):
                collection = ImageTitle.objects.create(title='banner')  # кастомний title
                setattr(self.object, self.formset_instance_attr, collection)
                self.object.save(update_fields=[self.formset_instance_attr])

            # Зберігаємо formset
            if formset.is_valid():
                formset.instance = getattr(self.object, self.formset_instance_attr)
                formset.save()

        return super().form_valid(form)


class BannerUpdateView(FormsetMixin, generic.UpdateView):
    model = Banner
    form_class = BannerForm
    template_name = "banner/banner_form.html"
    success_url = reverse_lazy("admin_panel:banner-list")
    formset_class = GalleryImageFormSet

    def get_queryset(self):
        return (
            Banner.objects
            .select_related("collection")  # JOIN для FK
            .prefetch_related("collection__images")  # всі картинки з колекції
        )

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        with transaction.atomic():
            # Зберігаємо основний об’єкт Banner
            self.object = form.save()

            # Перевірка наявності collection (якщо раптом його нема)
            if not getattr(self.object, self.formset_instance_attr):
                collection = ImageTitle.objects.create(title='banner')
                setattr(self.object, self.formset_instance_attr, collection)
                self.object.save(update_fields=[self.formset_instance_attr])

            # Зберігаємо formset
            if formset.is_valid():
                formset.instance = getattr(self.object, self.formset_instance_attr)
                formset.save()

        return super().form_valid(form)


class BannerDeleteView(generic.DeleteView):
    model = Banner
    template_name = "banner/banner_confirm_delete.html"
    success_url = reverse_lazy("admin_panel:banner-list")
