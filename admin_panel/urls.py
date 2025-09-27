from django.urls import path

from admin_panel.views import hello_world, SeoBlockListView, SeoBlockCreateView, SeoBlockUpdateView, SeoBlockDeleteView, \
    MainPageListView, MainPageCreateView, MainPageUpdateView, MainPageDeleteView, ContactPageListView, \
    ContactPageCreateView, ContactPageUpdateView, ContactPageDeleteView, NewsListView, NewsCreateView, NewsDeleteView, \
    NewsUpdateView, FilmListView, FilmCreateView, FilmDetailView, FilmUpdateView, FilmDeleteView

urlpatterns = [
    path("", hello_world, name="hello-world"),

    path("seo_block/", SeoBlockListView.as_view(), name="seo-block-list"),
    path("seo_block/create/", SeoBlockCreateView.as_view(), name="seo-block-create"),
    path("seo_block/update/<int:pk>/", SeoBlockUpdateView.as_view(), name="seo-block-update"),
    path("seo_block/delete/<int:pk>/", SeoBlockDeleteView.as_view(), name="seo-block-delete"),

    path("main/", MainPageListView.as_view(), name="main-page-list"),
    path("main/create/", MainPageCreateView.as_view(), name="main-page-create"),
    path("main/update/<int:pk>/", MainPageUpdateView.as_view(), name="main-page-update"),
    path("main/delete/<int:pk>/", MainPageDeleteView.as_view(), name="main-page-delete"),

    path("contact_page/", ContactPageListView.as_view(), name="contact-page-list"),
    path("contact_page/create/", ContactPageCreateView.as_view(), name="contact-page-create"),
    path("contact_page/update/<int:pk>/", ContactPageUpdateView.as_view(), name="contact-page-update"),
    path("contact_page/delete/<int:pk>/", ContactPageDeleteView.as_view(), name="contact-page-delete"),

    path("news/", NewsListView.as_view(), name="news-list"),
    path("news/create/", NewsCreateView.as_view(), name="news-create"),

    path("news/delete/<int:pk>/", NewsDeleteView.as_view(), name="news-delete"),
    path("news/update/<int:pk>/", NewsUpdateView.as_view(), name="news-update"),

    path("films/", FilmListView.as_view(), name="film-list"),
    path("films/create/", FilmCreateView.as_view(), name="film-create"),
    path("films/detail/<int:pk>/", FilmDetailView.as_view(), name="film-detail"),
    path("films/update/<int:pk>/", FilmUpdateView.as_view(), name="film-update"),
    path("films/delete/<int:pk>/", FilmDeleteView.as_view(), name="film-delete"),

]

app_name = "admin_panel"
