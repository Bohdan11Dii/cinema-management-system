from django.urls import path
from admin_panel.views import hello_world, SeoBlockListView, SeoBlockCreateView

urlpatterns = [
    path("", hello_world, name="hello_world"),
    path("seo_block/", SeoBlockListView.as_view(), name="seo_block_list"),
    path("seo_block/create?", SeoBlockCreateView.as_view(), name="seo_block_create"),
]

app_name = "admin_panel"