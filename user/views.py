from django.views import generic
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import UserCreateForm


class UserCreateView(generic.CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)  # закінчення сесії при закритті браузера
        return redirect(self.success_url)
