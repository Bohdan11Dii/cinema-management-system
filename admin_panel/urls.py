from django.urls import path

from admin_panel.views import hello_world, SeoBlockListView, SeoBlockCreateView, SeoBlockUpdateView, SeoBlockDeleteView, \
    MainPageListView, MainPageCreateView, MainPageUpdateView, MainPageDeleteView, ContactPageListView, \
    ContactPageCreateView, ContactPageUpdateView, ContactPageDeleteView

urlpatterns = [
    path("", hello_world, name="hello_world"),

    path("seo_block/", SeoBlockListView.as_view(), name="seo_block_list"),
    path("seo_block/create/", SeoBlockCreateView.as_view(), name="seo_block_create"),
    path("seo_block/update/<int:pk>/", SeoBlockUpdateView.as_view(), name="seo_block_update"),
    path("seo_block/delete/<int:pk>/", SeoBlockDeleteView.as_view(), name="seo_block_delete"),

    path("main/", MainPageListView.as_view(), name="main_page_list"),
    path("main/create/", MainPageCreateView.as_view(), name="main_page_create"),
    path("main/update/<int:pk>/", MainPageUpdateView.as_view(), name="main_page_update"),
    path("main/delete/<int:pk>/", MainPageDeleteView.as_view(), name="main_page_delete"),

    path("contact_page/", ContactPageListView.as_view(), name="contact_page_list"),
    path("contact_page/create/", ContactPageCreateView.as_view(), name="contact_page_create"),
    path("contact_page/update/<int:pk>/", ContactPageUpdateView.as_view(), name="contact_page_update"),
    path("contact_page/delete/<int:pk>/", ContactPageDeleteView.as_view(), name="contact_page_delete"),

]

app_name = "admin_panel"
