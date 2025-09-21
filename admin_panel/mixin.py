from django.db import transaction

from admin_panel.models import ImageTitle


class FormsetMixin:
    formset_class = None  # тут треба буде вказати конкретний FormSet у підкласі
    formset_instance_attr = 'collection'  # атрибут, до якого прив’язаний formset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            data['formset'] = self.formset_class(self.request.POST, self.request.FILES,
                                                 instance=getattr(self.object, self.formset_instance_attr, None))
        else:
            data['formset'] = self.formset_class(instance=getattr(self.object, self.formset_instance_attr, None))
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        with transaction.atomic():
            self.object = form.save()
            # створюємо collection, якщо його ще немає
            if not getattr(self.object, self.formset_instance_attr):
                collection = ImageTitle.objects.create(title=self.object.title)
                setattr(self.object, self.formset_instance_attr, collection)
                self.object.save(update_fields=[self.formset_instance_attr])
            # зберігаємо formset
            if formset.is_valid():
                formset.instance = getattr(self.object, self.formset_instance_attr)
                formset.save()
        return super().form_valid(form)
