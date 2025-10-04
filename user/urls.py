
from django.urls import path

from user.views import UserCreateView

urlpatterns = [
    path("registrations/", UserCreateView.as_view(), name="registration"),
]

app_name = "user"
